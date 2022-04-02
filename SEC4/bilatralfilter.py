import cv2
from matplotlib import pyplot as plt
img = cv2.imread('fingerprint.jpg')
img1 = cv2.imread('fingerwithnoise.png')
blur = cv2.bilateralFilter(img, 9, 9, 75, 75)
blur1 = cv2.bilateralFilter(img, 9, 9, 75.75)
plt.subplot(141), plt.imshow(img), plt.title('original')
plt.subplot(142), plt.imshow(blur), plt.title('Blured')
plt.subplot(143), plt.imshow(img1), plt.title('image 1')
plt.subplot(144), plt.imshow(blur1), plt.title('Blured 1')
plt.show()