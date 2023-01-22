def square(num):
  return num ** 2

def t(f):
  def g(x):
    return f(f(f(x)))
  return g 

print(t(square)(7))
