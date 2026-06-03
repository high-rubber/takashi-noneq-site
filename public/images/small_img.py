import cv2

img = cv2.imread("takashigoto_hotpot_c.jpg")
n = 3  # Make the image 1/3 of its original size

small = cv2.resize(
    img,
    dsize=None,
    fx=1.0 / n,
    fy=1.0 / n,
    interpolation=cv2.INTER_AREA,  # Recommended for shrinking
)

cv2.imwrite("output.jpg", small)
