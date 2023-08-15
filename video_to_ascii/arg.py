#!/usr/bin/python3

import sys

# The first element of sys.argv is the script name itself
script_name = sys.argv[0]

# The following elements are the command-line arguments
# For example, if you run: python script.py arg1 arg2 arg3
# sys.argv[1] will be 'arg1', sys.argv[2] will be 'arg2', and so on

# Print the script name
print("Script name:", script_name)

# Print the command-line arguments
for i, arg in enumerate(sys.argv[1:], start=1):
    print(f"Argument {i}: {arg}")

