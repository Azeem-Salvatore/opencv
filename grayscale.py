import cv2

img = cv2.imread('cat.jpeg')
op = img.copy()

gray = cv2.cvtColor(op, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

#blur = cv2.GaussianBlur(gray, (3,3), 0)

edge = cv2.Canny(gray, 290, 300)

cv2.imshow("Edge", edge)
cv2.waitKey(0)