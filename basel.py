#!/usr/bin/python3
from math import pi


def basel(n):
  s = 0
  for i in range(1, n + 1):
    s += 1/(i ** 2)

  return s


assert basel(1) == 1
assert basel(2) == 1 + 1/4
assert basel(3) == 1 + 1/4 + 1/9

b = (pi**2)/6
S = basel(100000)
print(b)
print(S)
print(b - S)

pi_est = (S * 6)**0.5
print(pi)
print(pi_est)
print(pi - pi_est)
