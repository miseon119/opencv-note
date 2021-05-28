import cv2
import numpy as np

im1 = cv2.imread('data/src/lena.jpg')
im2 = cv2.imread('data/src/rocket.jpg')

# Concatenate vertically
im_v = cv2.vconcat([im1, im1])

# Concatenate horizontally
im_h = cv2.hconcat([im1, im1])
