import cv2
from matplotlib import pyplot as plt
img = cv2.imread('fingerprint.jpg')
# sobel  on X axis .. k size >> Kernel Size

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# sobel on Y axis
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
# merge sobel x and Y
sobelImage= cv2.add(sobelX,sobelY)
plt.subplot(141), plt.imshow(img),
plt.title('Original Image')
plt.subplot(142),
plt.imshow(sobelX)
plt.title('Sobel X')
plt.subplot(143),
plt.imshow(sobelY),
plt.title('Sobel Y')
plt.subplot(144), plt.imshow(sobelImage)
plt.title('Sobel Image')
plt.show()



