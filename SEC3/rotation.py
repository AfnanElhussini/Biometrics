import cv2
import numpy as np
original_img = cv2.imread('fingerprint.jpg',0)
# Size of image
rows, cols = original_img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
ri = cv2.warpAffine(original_img, M, (rows, cols))
cv2.imshow('OI', original_img)
cv2.imshow('RI', ri)
cv2.waitKey()
cv2.destroyAllWindows()