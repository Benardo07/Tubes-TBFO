def parse(file_path):
    transitions = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 5:
                currentState, input_symbol, pop_stack, goToState, push_stack = parts

                # Split the push_stack values if they are separated by a comma
                push_stack = push_stack.split(',')

                # Create a key as a tuple of current state, input symbol, and top of the stack
                key = (currentState, input_symbol, pop_stack)

                # Add the transition to the dictionary
                transitions[key] = (goToState, push_stack)

    return transitions

transition = parse("tes.txt")


def validate_tokens(tokens, transitions, start_state):
    stack = ['Z']  # Initialize the stack with the starting symbol
    now_state = start_state

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

            if ((stack[-1] == 'NOSTR') or (stack[-1] == 'STR') or (now_state == "inEm" and token == '>') or (now_state == "inStrong" and token == '>') or (now_state == "inB" and token == '>') or (now_state == "inSmall" and token == '>') or (now_state == "inAbbr" and token == '>') or (now_state == "InTD" and token == '>') or (now_state == "InTH" and token == '>')) :
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
    if(stack[-1] == 'Z'):
        return True
    else:
        return False