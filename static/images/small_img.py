"""
This code resizez an image, for the use in the profile page of the website.
It takes a large image, makes it smaller, and saves it as a new file.
"""

import cv2

img = cv2.imread("tks2026_tus.jpg")
n = 5  # Make the image 1/5 of its original size

small = cv2.resize(
    img,
    dsize=None,
    fx=1.0 / n,
    fy=1.0 / n,
    interpolation=cv2.INTER_AREA,  # Recommended for shrinking
)

cv2.imwrite("index_img.jpg", small)
