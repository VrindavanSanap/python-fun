#!/usr/bin/python3

import re

pattern = r'^I'  # ^ denotes the beginning of the string

string = "I want to belive LK99"

if (res := re.match(pattern, string)):
  print(res.group(0))
