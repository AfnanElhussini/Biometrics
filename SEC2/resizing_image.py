import cv2
original_img = cv2.imread('colorFingerprint.jpg')
half = cv2.resize(original_img, (0 , 0), fx=0.5, fy=0.5)
bigger = cv2.resize(original_img, (1050, 1610))
stretch_near = cv2.resize(original_img, (780, 540),
          interpolation = cv2.INTER_NEAREST)
cv2.imshow('Original Image',  original_img)
cv2.imshow('Half Image', half)
cv2.imshow('BIG', bigger)
cv2.imshow("STRETCH_NEAR", stretch_near)

cv2.waitKey(0)
cv2.destroyWindow()