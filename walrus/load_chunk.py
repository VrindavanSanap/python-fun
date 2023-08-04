#!/usr/bin/python3

with open("./zen.txt") as f:
  while chunk := f.read(255):
    print(chunk)
