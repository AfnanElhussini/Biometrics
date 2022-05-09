import cv2
import numpy as np
img = cv2.imread('box.jpg')
gray = cv2.cvColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', gray)
corners = cv2.goodFeaturesToTrack(gray, 20, 0.01, 5)

corners = np.int0(corners)
print(corners)
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (0, 0, 255), -10)
    cv2.imshow('original', img)
cv2.waitKey()
cv2.destroyAllWindows()