#!/usr/bin/python3

def turing_machine(input_str):
    # Define the transition rules as a dictionary
    # The keys are tuples representing the current state and the current symbol
    # The values are tuples representing the next state, the symbol to write, and the direction to move
    transition_rules = {
        ('q0', '0'): ('q0', '0', 'R'),
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', ' '): ('q1', ' ', 'L'),
        ('q1', '0'): ('q2', '1', 'L'),
        ('q1', '1'): ('q1', '1', 'L'),
        ('q1', ' '): ('halt', ' ', 'N'),
        ('q2', '0'): ('q2', '0', 'L'),
        ('q2', '1'): ('q2', '1', 'L'),
        ('q2', ' '): ('q0', ' ', 'R'),
    }

    tape = list(input_str + ' ')  # Input string on the tape
    head = 0  # Head position
    state = 'q0'  # Initial state

    while state != 'halt':
        current_symbol = tape[head]
        if (state, current_symbol) in transition_rules:
            next_state, write_symbol, move_direction = transition_rules[(state, current_symbol)]
            tape[head] = write_symbol
            if move_direction == 'L':
                head -= 1
            elif move_direction == 'R':
                head += 1
            state = next_state
        else:
            print("Invalid transition")
            break

    result = ''.join(tape).strip()
    return result


# Test the Turing machine with input binary numbers
input1 = "101"
input2 = "110"
output = turing_machine(input1 + " " + input2)
print("Result:", output)

