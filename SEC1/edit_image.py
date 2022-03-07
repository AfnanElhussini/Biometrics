#Image Writing
import cv2
original_img = cv2.imread('img1.jpg')
gray_image= cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
gray_image2= cv2.imread('img1.jpg', 0)
cv2.imwrite('img2.png', gray_image2)
cv2.imwrite(r"C:\Users\afnan\Desktop\img2.png", gray_image2)

cv2.waitKey()
cv2.destroyAllWindows()