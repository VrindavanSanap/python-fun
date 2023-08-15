#!/usr/bin/python3


import numpy as np
from numba import njit

@njit
def possible(grid, x, y, n):
    for i in range(9):
        if grid[y][i] == n or grid[i][x] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True

@njit
def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(grid, x, y, n):
                        grid[y][x] = n
                        if solve(grid):
                            return True
                        grid[y][x] = 0
                return False
    return True

if __name__ == "__main__":
    grid = [[1, 2, 3, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    if solve(grid):
        print(np.matrix(grid))
    else:
        print("No solution exists.")

