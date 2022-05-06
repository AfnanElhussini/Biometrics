import cv2
from matplotlib import pylab as plt
img = cv2.imread('fingerprint.jpg')
# cv2.CV_64F matrixType is double
laplacian = cv2.Laplacian(img,cv2.CV_64F)

# using matplotlibrary for Edge Detection
plt.subplot(121), plt.imshow(img)
plt.title('original image')
plt.subplot(122),
plt.imshow(laplacian)
plt.title('Edit Image')
plt.show()
