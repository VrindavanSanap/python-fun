#!/usr/bin/python3
from math import sqrt
from numba import njit
from tqdm import tqdm 

@njit
def max_prime_fac(n):
  max_prime_fac = 0
  for i in range(1, 1 + n//2):
    if n%i == 0:
      max_prime_fac= i
  return max_prime_fac 


@njit()
def main(): 
  n = 0 
  its = int(10e1) + 1
  for i in (range(1, its)):
    if (sqrt(i) > max_prime_fac(i)):
      n += 1
      print(i, n)
main()
