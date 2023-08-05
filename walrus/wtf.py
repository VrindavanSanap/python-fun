#!/usr/bin/python3

def f(x):
  if x and x%2 == 0:
    return x**2
  else:
    return None

data = [1, 2, 3, 4, 5, None, 6, 7, None, 8, 9]
result_list = [y for x in data if (y := f(x)) is not None]

print(result_list)

