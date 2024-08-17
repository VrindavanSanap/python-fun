#!/usr/bin/env python3
import subprocess

# Simple command
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

# Print the output
print(result.stdout)
