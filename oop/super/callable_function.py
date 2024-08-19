class Greeter:
  def __init__(self, greeting):
    self.greeting = greeting

  def __call__(self, name):
    return f"{self.greeting}, {name}!!"


greeter = Greeter("Wassup")
print(greeter("Alice"))
