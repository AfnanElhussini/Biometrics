import cv2
from matplotlib import pylab as plt

img = cv2.imread('grayfingerprint.jpg', 0)
img2= 255-img
img_not = cv2.bitwise_not(img)
plt.subplot(1,3,1), plt.imshow(img, cmap='gray'), plt.title('image')
plt.subplot(1,3,2), plt.imshow(img, cmap='gray'), plt.title('invert1')
plt.subplot(1,3,3), plt.imshow(img, cmap='gray'), plt.title('invert2')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()