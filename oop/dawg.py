# /bin/local/env python3


class Dog:
  def __init__(self, name):
    self.name = name

  def bark(self):
    return "Woof!"


fido = Dog("fido")
print(fido.bark())
