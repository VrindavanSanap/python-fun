#!/usr/bin/python3

import matplotlib.pyplot as plt

def generate_square_spiral(size):
    x, y = 0, 0
    dx, dy = 1, 0
    spiral = [(x, y)]

    for _ in range(1, size):
        if abs(x) == abs(y) and (dx, dy) != (1, 0):
            dx, dy = -dy, dx  # Change direction if at a corner
        elif x > 0 and x == y + 1:
            dx, dy = -1, 0  # Adjust direction for outer square

        x, y = x + dx, y + dy
        spiral.append((x, y))

    return spiral

size = 100  # Number of points in the spiral
spiral_points = generate_square_spiral(size)
x, y = zip(*spiral_points)

plt.plot(x, y, marker='o', linestyle='-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Square Spiral')
plt.grid(True)
plt.show()

