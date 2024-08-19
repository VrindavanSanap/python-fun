#!/usr/bin/env python3
import sys
import time

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

image = Image.open("./blob.jpg")
image_arr = np.array(image)
st = time.time()
for i in range(image_arr.shape[0]):
  means = np.mean(image_arr[i], axis=1)
  sorted_indices = np.argsort(means)
  image_arr[i] = image_arr[i][sorted_indices]
print(f"Image sorted in {time.time() - st} seconds")
plt.imshow(image_arr)
plt.show()
