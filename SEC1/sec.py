from cv2 import cv2
img = cv2.imread('img2.png')
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()