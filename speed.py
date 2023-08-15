#!/usr/bin/python3

from itertools import product

def possible(grid, x, y, n):
    row = set(grid[y])
    column = set(grid[i][x] for i in range(9))
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    block = set(grid[y0 + i][x0 + j] for i in range(3) for j in range(3))
    return n not in (row | column | block)

def solve(grid):
    for y, x in product(range(9), repeat=2):
        if grid[y][x] == 0:
            for n in range(1, 10):
                if possible(grid, x, y, n):
                    grid[y][x] = n
                    if solve(grid):
                        return grid
                    grid[y][x] = 0  # Backtrack
            return None
    return grid

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

    solution = solve(grid)
    if solution is not None:
        for row in solution:
            print(row)
    else:
        print("No solution exists.")
