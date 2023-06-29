# We want to find sqrt of 9 
# It will always be be between a 

def sqrt_fn(x, a=2, tolerance=0.01):
  a1 = a
  a2 = x/a
  guess = (a1 + a2)/2
  error = x - guess**2 
  
  if abs(error) < tolerance: return guess
  
  if error < 0:
    # We have overshot
    next_guess = (min(a1, a1) + guess)/2
    return sqrt_fn(x, next_guess)
  if error > 0:
    # We have undershot
    next_guess = (max(a1, a2) + guess)/2
    return sqrt_fn(x, next_guess)

assert (sqrt_fn(9,3)) == 3
assert (sqrt_fn(10) - 10**0.5) < 0.1

print(sqrt_fn(9, 2))
