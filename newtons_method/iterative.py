# We want to find sqrt of 9 
# It will always be be between a 

def sqrt_fn(x, guess = 2, tolerance=0.001):
  error = x - guess**2 
  while (abs(error) > tolerance):
    a1 = guess
    a2 = x/guess
    guess = (a1 + a2)/2
 
  
    if error < 0:
      # We have overshot
      guess = (min(a1, a1) + guess)/2
    if error > 0:
      # We have undershot
      guess = (max(a1, a2) + guess)/2
      
    error = x - guess**2 
  return guess

assert sqrt_fn(9,3)  == 3
assert int(sqrt_fn(4)) == 2

