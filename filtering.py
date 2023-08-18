# Reference: https://learnopencv.com/image-filtering-using-convolution-in-opencv/
import cv2 
import numpy as np
img = cv2.imread('dog.jpg')


# filter2D() function can be used to apply kernel to an image.
# Where ddepth is the desired depth of final image. ddepth is -1 if...
# ... depth is same as original or source image.
kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])
filtered = cv2.filter2D(img,ddepth=-1,kernel=kernel)

cv2.imshow('original',img)
cv2.imshow('filtered',filtered)


# Blurring an Image using a Custom 2D-Convolution Kernel

kernel1 = np.ones((11,11),dtype=np.float32) / 121
print(kernel1)
blurr = cv2.filter2D(img,ddepth=-1,kernel=kernel1)
cv2.imshow('blur',blurr)


# Sharpening an Image Using Custom 2D-Convolution Kernels
kernel2 = np.array([[0, -1,  0],
                   [-1,  5, -1],
                    [0, -1,  0]])
sharp = cv2.filter2D(img,ddepth=-1,kernel=kernel2)
cv2.imshow('sharp',sharp)

cv2.waitKey(0)
