#!/usr/bin/python3


import numpy as np
from numba import njit
grid = [[0,0,0,2,6,0,7,0,1],
        [6,8,0,0,7,0,0,9,0], 
        [1,9,0,0,0,4,5,0,0], 
        [8,2,0,0,0,0,0,4,0], 
        [0,0,0,0,0,0,0,0,0], 
        [0,5,0,0,0,0,0,2,8], 
        [0,0,0,0,0,0,0,7,4], 
        [0,0,0,0,0,0,0,3,6], 
        [0,0,0,0,0,0,0,0,0]]
print(np.sum(grid))

def possible(x, y, n):
  global grid 
  for i in range(0, 9):
    if grid[y][i] == n:
      return False
  for i in range(0, 9):
    if grid[i][x] == n:
      return False  

  x0 = (x//3) * 3
  y0 = (y//3) * 3

  for i in range(0, 3):
    for j in range(0, 3):
      if grid[y0+i][x0+j] == n:
        return False
  return True

def solve():
  global grid 
  for y in range(9):
    for x in range(9):
      if grid[y][x] == 0:
        for n in range(1, 10):
          if possible(x, y, n):
            grid[y][x] = n
            print(np.matrix(grid))
            solve()
            grid[y][x] = 0  
        return 
 
print(np.matrix(grid))
solve()
print(grid)
