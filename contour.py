import imutils
import cv2

#Simple importing segment
img = cv2.imread("tetris.png")

#Conv to gray from BGR and taking thresh
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

#Finding Contour
contr = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contr = imutils.grab_contours(contr)
op = img.copy()

#Drawing and displaying the results
for c in contr:
    
    cv2.drawContours(op, [c], -1, (240,0,159), 3)

txt = "I Found {} different tetris!!!".format(len(contr))
cv2.putText(op, txt, (10,25), cv2.FONT_HERSHEY_COMPLEX, 0.7, (240,0,159), 2)
cv2.imshow("Contours", op)
cv2.waitKey(0)