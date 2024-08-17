#!/usr/bin/env python3
import subprocess

# More complex command
process = subprocess.Popen(['ping', '-c', '4', 'google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Get the output and error
stdout, stderr = process.communicate()

print(stdout.decode())
