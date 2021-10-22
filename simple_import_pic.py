import cv2
import imutils

#Reading image from file
image = cv2.imread("cat.jpeg")

#To get a particular pixel Value
(B,G,R) = image[100,100]
print("R={},G={},B={}".format(R,G,B))

#To extract ROI/crop
roi = image[24:128, 47:159] #Format used is [startY:endY, startX:endX]
cv2.imshow("ROI",roi)

#To resize 
resized = cv2.resize(image,(200,200))
cv2.imshow("Resized", resized)

#helps us to visualize the location of pixel and the colour tone respy
(h,w,d) = image.shape
# print("width={}, height={}, depth={}".format(w,h,d))
# cv2.imshow("Image", image)

#To resize without compromise
expectedwidth = 100
newheight = expectedwidth / w #actual width
newdimension = (expectedwidth, int(newheight * h)) #actual height
aspect_ratio = cv2.resize(image, newdimension)
cv2.imshow("Aspect Ratio", aspect_ratio)

# (nh,nw,nd) = aspect_ratio.shape

# print("The dimensions of original pic are as follows \
#     width={}, height={}, depth={}".format(w,h,d))

# print('\n')

# print("The dimensions of resized pic are as follows \
#     width={}, height={}, depth={}".format(nw,nh,nd))

#The above process can be done using imutils
easyresize = imutils.resize(image, width=100)
cv2.imshow("Resize using Imutils", easyresize)

#To rotate an image from centre
centre = (w // 2, h // 2)
rot_matrix = cv2.getRotationMatrix2D(centre, -60, 1)
rotated_img = cv2.warpAffine(image, rot_matrix, (w,h))
cv2.imshow("Rotated img", rotated_img)


#helps to exit the window by pressing any key
cv2.waitKey(0)
