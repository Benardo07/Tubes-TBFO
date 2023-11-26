class Transition:
    def __init__(self, initial_state, input_symbol, stack_top, final_state, push_symbol):
        self.initial_state = initial_state
        self.input_symbol = input_symbol
        self.stack_top = stack_top
        self.final_state = final_state
        self.push_symbol = push_symbol

def read_pda_file(file_path):
    transitions = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            if len(parts) == 5:
                transition = Transition(*parts)
                transitions.append(transition)
    return transitions

def find_matching_transitions(transitions, initial_state, final_state):
    matching_transitions = []
    for transition in transitions:
        if transition.initial_state == initial_state and transition.final_state == final_state:
            matching_transitions.append(transition)
    return matching_transitions

def main():
    file_path = 'diagram.txt'  
    transitions = read_pda_file(file_path)

    initial_state = input("Enter the initial state: ")
    final_state = input("Enter the final state: ")

    matching_transitions = find_matching_transitions(transitions, initial_state, final_state)

    if matching_transitions:
        print("Matching Transitions:")
        for t in matching_transitions:
            print(f"{t.input_symbol},{t.stack_top}/{t.push_symbol}")
    else:
        print("No matching transitions found.")

if __name__ == "__main__":
    main()
