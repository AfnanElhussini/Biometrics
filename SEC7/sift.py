import cv2
from matplotlib import pyplot as plt

img = cv2.imread('fingerprint.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
kp = sift.detect(gray, None)
img1 = cv2.drawKeypoints(gray, kp, img)
cv2.imwrite('SIFT2.jpg', img1)
plt.imshow(img1)
plt.show()



