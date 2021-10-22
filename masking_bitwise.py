import cv2
import imutils

#Simple image importing snippet with BGR2GRAY and thresh funcns
img = cv2.imread("tetris.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

#Masking using bitiwse and
mask = thresh.copy()
op = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Masked Image", op)
cv2.waitKey(0)