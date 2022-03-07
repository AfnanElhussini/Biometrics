import cv2
originalImage = cv2.imread('bgr.jpg')
# SPLIT
B, G, R= cv2.split(originalImage)
cv2.imshow('Original Image', originalImage)
cv2.imshow("Blue",B)
cv2.imshow("RED", R)
cv2.imshow("GREEN", G)
# MERGE
m = cv2.merge((B, R, G))
cv2.imshow('Merged Color', m)
cv2.waitKey()
cv2.destroyWindow()