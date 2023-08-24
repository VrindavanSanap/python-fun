#!/usr/bin/python3
import numpy as np

np.set_printoptions(precision=1)
spiral = np.zeros((11, 11))


def gen_spiral_coords(n):
    x, y = 0, 0 
    dx, dy = 0, -1
    return [(x, y) for _ in range(n) if (x := x + dx) >= 0 and (y := y + dy) >= 0 and
            (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)] or (x, y) == (1 - y, x)]

for i in gen_spiral_coords(2):
  
  #print(np.matrix(spiral))

  print(i[0], i[1])
