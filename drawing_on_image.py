import cv2

img = cv2.imread('cat.jpeg')
(h, w, d) = img.shape

op = img.copy()
op = cv2.rectangle(op, (40,21), (160,130), (0,0,255), 2)
cv2.imshow("Box", op)

cv2.waitKey(0)

