import cv2

img = cv2.imread("cat.jpeg")

op = cv2.putText(img, "A Fuckin Cat !!!!", (5,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
cv2.imshow("cat", op)
cv2.waitKey(0)