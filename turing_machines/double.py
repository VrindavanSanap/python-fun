#!/usr/bin/python3
def turing_machine(tape):
  """Doubling any series of 1s encountered on a tape."""

  head = 0
  while head < len(tape):
    if tape[head] == "1":
      tape[head] = "0"
      head += 1
      tape[head] = "1"
    else:
      head += 1

  return tape


if __name__ == "__main__":
  tape = "111"
  print(turing_machine(tape))

