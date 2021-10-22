import cv2

img = cv2.imread("flowers.jpeg")
en_img = 2 * img
cv2.imshow("img", img)
cv2.imshow("en_img", en_img)
cv2.waitKey(0)