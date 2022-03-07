import cv2
# Gray
original_image= cv2.imread('colorFingerprint.jpg')
grayImage= cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
# Binary
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Image', original_image)
cv2.imshow('Gray Image', grayImage)
cv2.imshow('Binary Image', blackAndWhiteImage)
cv2.waitKey()
cv2.destroyAllWindows()
