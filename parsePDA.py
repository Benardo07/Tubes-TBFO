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

transition = parse("tes.txt")


def validate_tokens(tokens, PDA):
    start_state = PDA["start_state"]
    transitions = PDA["transitions"]
    pda_type = PDA["pda_type"]
    stack = ['Z']  # Initialize the stack with the starting symbol
    now_state = start_state

    tempState = ['InH1','InH2','InH3','InH4','InH5','InH6','InP','InTable','inEm','inStrong','inB','inSmall','inAbbr','InTD','InTH','InButton','InDiv','InForm','InA']
    for token in tokens:
        print("Processing token:", token)
        print("Current stack:", stack)
        print("Current state:", now_state)

        # Modify the key to include the top of the stack
        key = (now_state, token, stack[-1] if stack else 'Z')  # Assuming 'Z' is the stack's empty symbol

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

            if ((stack[-1] == 'NOSTR') or (stack[-1] == 'STR') or ((now_state in tempState) and  token == '>')):
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
            print("Invalid transition for token:", token)
            return False  # Invalid transition

    # The input is valid if all tokens are processed successfully
    if(stack[-1] == 'Z' and pda_type =='E'):
        return True
    else:
        return False
    

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
        
        for char in file.read():
            if isInPetik and char != '"':
                if strictString :
                    if(char != ' '):
                        temp += char
                if(char != ' '):
                    tempIsi = 'str'  
            elif isDalamKomentar and char == ' ' :
                temp = ''
            elif char == '-':
                if isDalamKomentar and firstMin:
                    temp = ''
                    temp += char
                    firstMin = False
                else :
                    temp += char
                    firstMin = True
                if(temp == "<!--"):
                    isDalamKomentar = True
                    token.append(temp)
                    temp = ''             
            elif char == '<':
                if(temp != ''):
                    token.append('str')
                    temp=''
                temp += char
                closetag = False
            elif char == '>' :
                if(isDalamKomentar):
                    temp += char
                    if(temp == "-->"):
                        token.append(temp)
                        temp = ''
                        isDalamKomentar = False
                else : 
                    if(temp != ''):
                        token.append(temp)
                        temp=''
                    token.append(char)
                    closetag = True
            elif  char == "=" and not(closetag):
                if(temp != ''):
                    if(temp == 'method' or temp == 'type'):
                        strictString = True
                    token.append(temp)
                    temp = ''
                token.append(char)
            elif char == '"' and isInPetik:
                if(strictString):
                    strictString = False
                else:
                    temp += tempIsi
                temp += char
                token.append(temp)
                temp =''
                tempIsi = 'nostr'
                isInPetik = False
            elif char == '"' and not(closetag):
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
                    token.append(temp)
                    temp = ''

    if(temp != '' and isInPetik):
        token.append(temp)
        temp = ''

    return token