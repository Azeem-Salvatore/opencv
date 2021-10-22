import cv2
import imutils

#Simple image importing snippet with BGR2GRAY and thresh funcns
img = cv2.imread("tetris.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

#Erosion
eroded = cv2.erode(thresh, None, iterations=15)
cv2.imshow("Eroded Image:", eroded)

#Dilation
dilated = cv2.dilate(thresh, None, iterations=5)
cv2.imshow("dilated image", dilated)

cv2.waitKey(0)