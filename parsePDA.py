
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BLUE = "\033[34m"   # Blue text
MAGENTA = "\033[35m" # Magenta text
CYAN = "\033[36m"    # Cyan text
WHITE = "\033[37m"   # White text

def parse(file_path):
    PDA = {
        "all_states": [],
        "input_symbols": [],
        "stack_symbols": [],
        "start_state": "",
        "start_stack_symbol": "",
        "final_state": "",
        "pda_type": "",
        "transitions": {}
    }

    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Parse initial configuration
        PDA["all_states"] = lines[0].strip().split()
        PDA["input_symbols"] = lines[1].strip().split()
        PDA["stack_symbols"] = lines[2].strip().split()
        PDA["start_state"] = lines[3].strip()
        PDA["start_stack_symbol"] = lines[4].strip()
        PDA["final_state"] = lines[5].strip()
        PDA["pda_type"] = lines[6].strip()

        # Parse transitions
        for line in lines[7:]:
            parts = line.strip().split()
            if len(parts) == 5:
                currentState, input_symbol, pop_stack, goToState, push_stack = parts

                # Split the push_stack values if they are separated by a comma
                push_stack = push_stack.split(',')

                # Create a key as a tuple of current state, input symbol, and top of the stack
                key = (currentState, input_symbol, pop_stack)

                # Add the transition to the dictionary
                PDA["transitions"][key] = (goToState, push_stack)

    return PDA



def validate_tokens(tokens, PDA):
    start_state = PDA["start_state"]
    transitions = PDA["transitions"]
    pda_type = PDA["pda_type"]
    stack = ['Z']  # Initialize the stack with the starting symbol
    now_state = start_state

    tempState = ['InH1','InH2','InH3','InH4','InH5','InH6','InP','InTable','inEm','inStrong','inB','inSmall','inAbbr','InTD','InTH','InButton','InDiv','InForm','InA','InScript']
    for token in tokens:
        # Modify the key to include the top of the stack
        key = (now_state, token[0], stack[-1] if stack else 'Z')  # Assuming 'Z' is the stack's empty symbol

        if key in transitions:
            goToState, push_stack = transitions[key]

            # Pop from the stack as the transition was found
            stack.pop()

            # Change the current state
            now_state = goToState

            # Push new elements onto the stack in reverse order
            for element in reversed(push_stack):
                if element != 'e':  # Assuming 'e' is the symbol for 'do nothing'
                    stack.append(element)
            if ((stack[-1] == 'NOSTR') or (stack[-1] == 'STR') or ((now_state in tempState) and  token[0] == '>')):
                while True:
                    special_key = (now_state, 'e', stack[-1] if stack else 'Z')
                    if special_key in transitions:
                        goToState, push_stack = transitions[special_key]
                        stack.pop()  # Pop the current top element
                        now_state = goToState
                        for element in reversed(push_stack):
                            if element != 'e':
                                stack.append(element)
                    else:
                        break  # No more transitions for 'e' input
        else:
            result = False
            valid_transitions = [(k, v) for k, v in transitions.items() if k[0] == now_state and k[2] == stack[-1]]
            if(token[0] == '<body' and stack[-1] == 'CHtml'):
                 expected_inputs = set([k[1] for k, v in valid_transitions if k[1] != '<!--' and not k[1].startswith('</')])
            elif (stack[-1] == "id" or stack[-1] == "Class" or stack[-1] == "Style" or stack[-1] == "id" or stack[-1] == "Href" or stack[-1] == 'Source' or stack[-1] == 'Rel'):
                expected_inputs = "="
            else:
                expected_inputs = set([k[1] for k, v in valid_transitions if len(v[1]) == 1 and v[1][0] != stack[-1]])

            


            # Extract possible input symbols that would lead to pushing 'e'
            if(stack[-1] == '=' and stack[-2] != 'BForm'):
                expected_inputs = '"'
                return result,'"str"',token[1],stack[-1],expected_inputs
            else:
                return result,token[0],token[1],stack[-1] ,expected_inputs # Invalid transition

    # The input is valid if all tokens are processed successfully
    if(stack[-1] == 'Z' and pda_type =='E'):
        result = True
        return result,token[0],token[1],stack[-1],None
    else:
        result = False
        valid_transitions = [(k, v) for k, v in transitions.items() if k[0] == now_state and k[2] == stack[-1]]

        expected_inputs = set([k[1] for k, v in valid_transitions if len(v[1]) == 1 and v[1][0] != stack[-1]])

        return result,token[0],token[1],stack[-1],expected_inputs
        
        
    
    
    

def parseHTML(html_file):
    with open(html_file, 'r') as file:
        token = []
        temp = ''
        tempIsi = 'nostr'
        isInPetik = False
        isDalamKomentar = False
        closetag = False
        strictString = False
        firstMin = True
        line_number = 0
        lines = []
        temp_cadangan = ''
        for line in file:
            line_number += 1
            lines.append(line)  # Store the current line
        
            for char in line:


                if isInPetik and char != '"':
                    if strictString :
                        if(char != ' '):
                            temp += char
                    if (char != ' '):
                        tempIsi = 'str'  
                    temp_cadangan += char
                elif isDalamKomentar and char == ' ' :
                    temp = ''
                elif char == '-':
                    if isDalamKomentar and firstMin:
                        temp = ''
                        temp += char
                        firstMin = False
                    else :
                        temp += char
                    if(temp == "<!--"):
                        isDalamKomentar = True
                        token.append((temp,line_number))
                        temp = '' 
                        firstMin = True            
                elif char == '<':
                    if(temp != ''):
                        token.append(('str',line_number-1))
                        temp=''
                    temp += char
                    closetag = False
                elif char == '>' :
                    if(isDalamKomentar):
                        temp += char
                        if(temp == "-->"):
                            token.append((temp,line_number))
                            temp = ''
                            isDalamKomentar = False
                            closetag = True
                    else : 
                        if(temp != ''):
                            token.append((temp,line_number))
                            temp=''
                        token.append((char,line_number))
                        closetag = True
                elif  char == "=" and not(closetag):
                    if(temp != ''):
                        if(temp == 'method' or temp == 'type'):
                            strictString = True
                        token.append((temp,line_number))
                        temp = ''
                    token.append((char,line_number))
                elif char == '"' and isInPetik:
                    if(strictString):
                        strictString = False
                    else:
                        temp += tempIsi
                    temp += char
                    token.append((temp,line_number))
                    temp =''
                    tempIsi = 'nostr'
                    isInPetik = False
                    temp_cadangan = ''
                elif char == '"' and not(closetag):
                    temp_line = line_number
                    temp += char
                    isInPetik = True
                elif  char != " " and char != "\n":
                    temp += char
                elif char == " ":
                    if(closetag) and char != '\n' and char != ' ':
                        temp  += char
                    elif not(closetag) and (temp != '') and not(isDalamKomentar):
                        if(temp == 'method' or temp == 'type'):
                            strictString = True
                        token.append((temp,line_number))
                        temp = ''

    if(temp != '' and isInPetik):
        token.append((temp_cadangan,temp_line))
        temp = ''

    return token,lines


def output_to_terminal(validate,inputError,lineNumber,stack_symbol,expected,lineHTML,PDA):
    if(validate):
        print()
        print(GREEN + "ACCEPTED" +YELLOW + " --Your HTML file has been validated True" + RESET)
        print()

    else:
        print()
        print(RED + "REJECTED" + RESET)
        print(RED + "Error in Line number " + str(lineNumber) + RESET)
        print(YELLOW +"      Line " + str(lineNumber) + " : ",end="")
        print(YELLOW + lineHTML[lineNumber-1] + RESET)

        if not(inputError in PDA["input_symbols"]):
            print(BLUE + "Invalid syntax at " + GREEN + inputError + RESET)
        elif (inputError == 'str' and stack_symbol != 'COM'):
            print(BLUE + "Invalid string " + WHITE + "--" + YELLOW + " String can't be there !!" + RESET)
        elif(stack_symbol == 'COM'):
            print(BLUE + "Expected this following elements: " + GREEN + "-->" + BLUE + " after " + YELLOW + inputError + RESET)  
        else:
            if expected:
                expected_inputs = ", ".join(expected)
                print(BLUE + "Expected this following elements: " + GREEN +expected_inputs + BLUE + " before " + YELLOW + inputError + RESET)
                print()
