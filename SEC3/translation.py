import numpy as np
import cv2
original_img = cv2.imread('fingerprint.jpg',0)
# Size of image
rows, cols = original_img.shape
print(rows, cols)
M = np.float32([[1, 0, 50], [0, 1, 50]])
ti= cv2.warpAffine(original_img, M, (rows, cols))
cv2.imshow('Original Image', original_img)
cv2.imshow('Translation Image', ti)
cv2.waitKey()
cv2.destroyAllWindows()