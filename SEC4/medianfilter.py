import cv2
from matplotlib import pyplot as plt

img = cv2.imread('finger.png.jpg')
blur = cv2.medianBlur(img, 5)
plt.subplot(121), plt.imshow(img), plt.title('Original image')
plt.subplot(121), plt.imshow(blur), plt.title('Bluer')
plt.show()

