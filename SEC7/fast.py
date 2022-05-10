import cv2
from matplotlib import pyplot as plt
img = cv2.imread('fingerprint.jpg')
fast = cv2.FastFeatureDetector_create()
# find and draw keypoints
kp = fast.detect(img, None)
img2= cv2.drawKeypoints(img, kp, None)
print("Total Key-Point:{}".format(len(kp)))
cv2.imwrite('fast-image.jpg', img2)
plt.imshow(img2)
