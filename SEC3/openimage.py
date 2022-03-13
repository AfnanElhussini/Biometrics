import cv2
import numpy as np
original_img = cv2.imread('fingerprint.jpg', 0)
(th, bi) = cv2.threshold(original_img, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((3, 3), np.uint8)
oi= cv2.morphologyEx(bi, cv2.MORPH_OPEN, kernel)
# cv2.imshow('OI', original_img)
cv2.imshow('BI', bi)
cv2.imshow('OI', oi)
cv2.waitKey()
cv2.destroyAllWindows()