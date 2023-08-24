import matplotlib.pyplot as plt

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def ulam_spiral(size):
    spiral = [[0] * size for _ in range(size)]
    x, y = size // 2, size // 2
    num = 1
    step = 1
    spiral[x][y] = num
    
    while step < size:
        for _ in range(step):
            x += 1
            num += 1
            if is_prime(num):
                spiral[x][y] = num
        
        for _ in range(step):
            y -= 1
            num += 1
            if is_prime(num):
                spiral[x][y] = num
        
        step += 1
        
        for _ in range(step):
            x -= 1
            num += 1
            if is_prime(num):
                spiral[x][y] = num
        
        for _ in range(step):
            y += 1
            num += 1
            if is_prime(num):
                spiral[x][y] = num
        
        step += 1
    
    return spiral

def plot_ulam_spiral(spiral):
    plt.imshow(spiral, cmap='viridis', interpolation='none')
    plt.colorbar()
    plt.title("Ulam Spiral")
    plt.show()

size = 5001# Adjust the size of the spiral as needed
spiral = ulam_spiral(size)
plot_ulam_spiral(spiral)

