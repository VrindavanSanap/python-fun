#!/usr/bin/python3
from PIL import Image
import numpy as np
import sys

image_path = "x-ray.jpg"
if len(sys.argv) == 2:
  image_path = sys.argv[1]
image = Image.open(image_path)

new_size = (120, 60)  
resized_image = image.resize(new_size)
gray_resized_image = resized_image.convert("L")
gray_resized_array = np.array(gray_resized_image, dtype=float)
gray_resized_array /= 255
ASCII_CHARS = "@%#*+=-:. "
l = (len(ASCII_CHARS ))
gray_resized_array *= l-1
gray_resized_array =  np.array(gray_resized_array, dtype=int)
print(gray_resized_array.max(), gray_resized_array.min())
ascii_art = ""
for i in gray_resized_array:
  for j in i:
    print(ASCII_CHARS[j] , end = "")
  print()
