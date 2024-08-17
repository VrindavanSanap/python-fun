#!/usr/bin/env python3
class Point:
  __match_args__ = ("x", "y")

  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y


def where_is(point):
  # point is an (x, y) tuple
  match point:
    case Point(0, 0):
      print("Origin")
    case Point(0, y):
      print(f"Y={y}")
    case Point(x, 0):
      print(f"X={x}")
    case Point(x, y):
      print(f"X={x} Y={y}")

    case Point():
      print("Somewhere else")
    case _:
      print("Not a point")


a = Point(1, 2)
b = Point(0, 21)
c = Point(1, 0)
where_is(a)
where_is(b)
where_is(c)
