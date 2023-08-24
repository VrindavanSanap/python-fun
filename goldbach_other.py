#!/usr/bin/python3

#
# Breaking goldbachs other conjecture ie.
# every odd composite number can be written as
# the sum of prime and twice a square.
#


from sympy import isprime
import math

def odd_composite():
    num = 9
    while True:
        if not isprime(num):
          yield num
        num += 2

def primes():
    num = 2
    while True:
        if isprime(num):
            yield num
        num += 1

is_square = lambda n : math.sqrt(n).is_integer()
  
n1 = 9 
n2 = 15
assert is_square(n1)
assert not is_square(13)

is_twice_square = lambda n : is_square(n/2)
assert is_twice_square(200)
assert not is_twice_square(199)

def prime_twice_square(n):
  for p in primes():
    if p > n:
      break
    if is_twice_square(n - p):
      print(f"{n} = {p} + 2 * {math.sqrt((n-p)/2)}^2")
      return True
  return False


for c in odd_composite():
   if not prime_twice_square(c):
    print(f"Broken on {c}")
    break 
