#!/usr/bin/env python3
# American Roulette
import random
from collections import namedtuple

Roulette_number = namedtuple("R_num", "number color")


class Roulette:
  COLORS = "red black green".split()
  NUMBERS = "0-28-9-26-30-11-7-20-32-17-5-22-34-15-3-24-36-13-1-00-27-10-25-29-12-8-19-31-18-6-21-33-16-4-23-35-14-2".split("-")

  def __init__(self):
    self.nums = [
      Roulette_number(num, "green")
      if num in self.NUMBERS[::19]
      else Roulette_number(num, "red")
      if int(num) % 2 != 0 and num != "0"
      else Roulette_number(num, "black")
      for num in self.NUMBERS
    ]

  def spin(self):
    return random.choice(self.nums)


r = Roulette()
res = r.spin()
print(res)
