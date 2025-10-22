import cv2
import numpy as np

# Read image
img = cv2.imread('p3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binarize (black ink = 255 after invert)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Suppose you want to paste at x-coordinate = 100
x = 100
column = thresh[:, x]  # all pixels in this column
y_candidates = np.where(column > 0)[0]  # indexes of black pixels

if len(y_candidates) > 0:
    y = y_candidates[0]  # first black pixel in this column
else:
    y = 0  # default if column empty

print("Paste at (x, y):", x, y)
