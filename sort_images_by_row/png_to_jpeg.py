#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

IMG_LOC = "./blob.png"

# Open the PNG image
png_image = Image.open(IMG_LOC)

# Convert PNG to RGB (JPEG does not support transparency)
rgb_image = png_image.convert("RGB")

# Save the image as a JPEG file
rgb_image.save(IMG_LOC.replace(".png", ".jpg"), "JPEG")
