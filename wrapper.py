#!/usr/bin/env python3


def add_wrapping(item):
  def wrapped_item():
    return f"A wrapped up box of {item()}"

  return wrapped_item


@add_wrapping
def new_gpu():
  return "A new Nvidia 3090"


print(new_gpu())
