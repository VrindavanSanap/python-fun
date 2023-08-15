#!/usr/bin/python3

tape = "001101010"

def tm(tape, pos):
  assert pos < len(tape)
  print(tape[pos])

tm(tape, 2)
