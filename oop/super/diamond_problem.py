class Engine:
  def make_sound(self):
    print("Generic sound")


class Car(Engine):
  def make_sound(self):
    print("Horn sound")


class Robot(Engine):
  def make_sound(self):
    print("Robot sound")


class Transformer(Car, Robot):
  pass


t = Transformer()
t.make_sound()

print(Transformer.mro())
