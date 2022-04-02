import cv2
from matplotlib import pyplot as plt
img =cv2.imread('fingerprint.jpg')
blured = cv2.GaussianBlur(img, (5,5), 0)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(121), plt.imshow(blured), plt.title('Bluerd')
plt.show()
