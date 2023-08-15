#!/usr/bin/python3


def countdown():
    n = 0 
    while True:
        yield n
        n -= 1

# Using the generator
for i in countdown():
    print(i)

