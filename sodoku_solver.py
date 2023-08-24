#!/usr/bin/python3

#
# From the computerphile video
# is slow af send help!!
#

import numpy as np
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

    row = any(grid[y][i] == n for i in range(9))
    column = any(grid[i][x] == n for i in range(9))

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    square = any(grid[y0 + i][x0 + j] == n for i in range(3) for j in range(3))

    return not (row or column or square)

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
 
print(np.matrix(grid))
solve()
print(grid)
