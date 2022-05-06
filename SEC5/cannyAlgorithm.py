import cv2
from matplotlib import pyplot as plt
img = cv2.imread('fingerprint.jpg')
# here Canny takes the image and 2 thresholds
edges = cv2.Canny(img, 100, 200)
plt.subplot(121),
plt.imshow(img)
plt.title('Original Image')
plt.subplot(122)
plt.imshow(edges)
plt.title('Edge Image')
plt.show()