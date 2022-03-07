import cv2
bgrImage= cv2.imread('bgr.jpg')
hsvImage= cv2.cvtColor(bgrImage, cv2.COLOR_BGR2HSV)
cv2.imshow('BGR Image', bgrImage)
cv2.imshow('HSV Image', hsvImage)

H= hsvImage[:, :, 0]
S= hsvImage[:, :, 1]
V= hsvImage[:, :, 2]
cv2.imshow('HSV Image', hsvImage)
cv2.imshow('Hue', H)
cv2.imshow('Vue', V)
cv2.imshow('Saturation', S)
cv2.waitKey()
cv2.destroyWindow()

