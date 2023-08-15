#!/usr/bin/python3


class TuringMachine:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_state = initial_state
        self.final_states = final_states

    def run(self, input_string):
        tape = list(input_string)
        head = 0

        while self.current_state not in self.final_states:
            current_symbol = tape[head]

            if (self.current_state, current_symbol) not in self.transitions:
                raise Exception("No transition defined for current state and symbol.")

            transition = self.transitions[(self.current_state, current_symbol)]
            tape[head] = transition[1]  # Write new symbol

            if transition[2] == 'R':
                head += 1
                if head == len(tape):
                    tape.append('_')
            elif transition[2] == 'L':
                head -= 1
                if head < 0:
                    tape.insert(0, '_')

            self.current_state = transition[0]  # Transition to new state

        return ''.join(tape)


# Define the Turing machine
states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transitions = {
    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', '1'): ('q0', '1', 'R'),
    ('q0', '_'): ('q1', '1', 'L'),
    ('q1', '0'): ('q2', '1', 'L'),
    ('q1', '1'): ('q1', '0', 'L'),
    ('q2', '0'): ('q2', '0', 'L'),
    ('q2', '1'): ('q2', '1', 'L'),
    ('q2', '_'): ('q0', '1', 'R'),
}
initial_state = 'q0'
final_states = {'q0'}

tm = TuringMachine(states, alphabet, transitions, initial_state, final_states)
input_string = '1101'
result = tm.run(input_string)
print(f"Input: {input_string}\nOutput: {result}")

