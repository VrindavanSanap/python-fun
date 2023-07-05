def f(x):
  return x**5 + x**2 - x - 0.2

def get_derivative_function(f):
  h = 0.00001
  def df(x):
    return (f(x + h) - f(x))/h
  
  return df

df = get_derivative_function(f)
guess = 1.3
for i in range(100):
  
  step = f(guess)/df(guess)
  guess = guess - step
  
  print(guess, f(guess))
