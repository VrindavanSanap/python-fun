#!/usr/bin/python3

def simple(s):
  #Given state s returns next state of the same size 
  assert isinstance(s, list)
  n_s = ['0'] * len(s)
  for i in range(len(s)):
    if i == 0 or i == len(s) - 1:
      n_s[i] = '0'
    else:
      if  s[i-1:i+2] == ['1', '1', '1']:
        n_s[i] = '1'
      if  s[i-1:i+2] == ['0', '1', '0']:
        n_s[i] = '1'
      if  s[i-1:i+2] == ['1', '1', '0']:
        n_s[i] = '0'
      if  s[i-1:i+2] == ['1', '0', '1']:
        n_s[i] = '0'
      if  s[i-1:i+2] == ['1', '0', '0']:
        n_s[i] = '0'
      if  s[i-1:i+2] == ['0', '1', '1']:
        n_s[i] = '0'
      if  s[i-1:i+2] == ['0', '0', '1']:
        n_s[i] = '0'
      if  s[i-1:i+2] == ['0', '0', '0']:
        n_s[i] = '0'
  return n_s

def print_state(s):
  for i in s:
    if i == "1":
      print("#", end="")
    else:
      print("-", end="")
  print()

def get_start_state(n):
  s = ["0", "0"]
  for i in range(n):
    s.insert(1, "1")
  return s

assert get_start_state(2) == ["0", "1", "1", "0"]
if __name__ == "__main__":
  import sys
  print(sys.argv)
  if not len(sys.argv) == 2:
    print("ussage <n>")
    exit(-1)
  n = sys.argv[1]
  s = get_start_state(int(n))
  print_state(s)
  for i in range(20): 
    s = simple(s)
    print_state(s)

 
