#!/usr/bin/python3

import sys

class WithoutSlots:
    def __init__(self):
        self.data = [0] * 100

class WithSlots:
    __slots__ = ("data",)
    def __init__(self):
        self.data = [0] * 100

# Create instances of both classes
without_slots = WithoutSlots()
with_slots = WithSlots()

# Get memory usage of each instance
print("Memory usage without __slots__:", sys.getsizeof(without_slots))
print("Memory usage with __slots__:", sys.getsizeof(with_slots))

print(without_slots.__dict__)
try:
  print(with_slots.__dict__)
except:
  print("no dict")
