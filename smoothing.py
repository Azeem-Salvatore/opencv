import cv2

# #Extracting ROI
# roi = image[20:125, 50:160]

#Smoothing the ROI using gausian blur
def smoothening(image):
    g_blur_0 = cv2.GaussianBlur(image, (11,11), 0)
    return g_blur_0

#importing an image
image = cv2.imread("cat.jpeg")
cv2.imshow("Smoothened Image", smoothening(image))