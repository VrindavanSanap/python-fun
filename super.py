#!/usr/bin/env python3
class Animal:
  def sound(self):
    print("The animal makes a sound")


class Dog(Animal):
  def sound(self):
    # We have overridden the sound method of the animal class
    # but we can still call it
    super().sound()
    print("WOff! woff!!")


dawg = Dog()
dawg.sound()
