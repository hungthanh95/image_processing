import cv2

# load img
image = cv2.imread("./img/jurassic-park-tour-jeep.jpg")
cv2.imshow("original", image)

# print dimensions of the image
print("Original size: " + str(image.shape))

# Output: (388, 647, 3)
# 388 rows, 647 columns and 3 channels RGB
# => 647 pixel wide and 388 pixel tall


# resizing an image
# ratio
r = 100.0 / image.shape[1]
dim = (100, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation  =cv2.INTER_AREA)
cv2.imshow("resized", resized)
print("Resized: " + str(resized.shape))

# Rotating an image
# grab the dimensions of the image and calculate center
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

# rotate the image 180 degrees
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("rotated", rotated)


# crop image
cropped = image[70:170, 440:540]
cv2.imshow("Cropped", cropped)

cv2.waitKey(0)