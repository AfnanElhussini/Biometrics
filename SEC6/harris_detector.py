import cv2
import numpy as np
img = cv2.imread('box.jpg')
# corners detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corners = cv2.cornerHarris(gray, 2, 3, 0.04)
corners = cv2.dilate(corners, None)
th = corners > 0.01 * corners.max()
img[th] = [0, 0, 255]
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

