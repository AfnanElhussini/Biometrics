#Image Reading

from cv2 import cv2
original_img = cv2.imread('img1.jpg')
gray_image= cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
gray_image2= cv2.imread('img1.jpg', 0)

cv2.imshow('Gray Image', gray_image)
cv2.imshow('Original Image', original_img)
cv2.imshow('Gray Image2', gray_image2)
cv2.waitKey()
cv2.destroyAllWindows()
