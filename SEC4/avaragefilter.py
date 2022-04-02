import cv2
from matplotlib import pylab as plt
# original image
img = cv2.imread('fingerwithnoise.png')
# image after filtering
blur = cv2.blur(img, (5, 5))

plt.subplot(121), plt.imshow(img), plt.tile('Original image')
plt.subplot(122), plt.imshow(blur), plt.tile('Blurred image')
plt.show()

