# Reference : https://learnopencv.com/contour-detection-using-opencv-python-c/

'''
steps:
1. read image and convert to gray scale
2. apply binary thresolding 
3. find the contours using findContours() method
4. draw contours using drawContours() method
'''

import cv2
import numpy as np

# reading image
img = cv2.imread('GettyImages-469196054-e1691415831480.webp')

# converting to gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# applying binary thresolding
ret,thresh = cv2.threshold(gray,250,250,cv2.THRESH_BINARY)

# find contours
contours, hierarchy = cv2.findContours(thresh,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

# draw contours
draw = cv2.drawContours(img,contours,contourIdx=-1,color=(0,255,0),thickness=3)
cv2.imshow('all contours',draw)


cv2.waitKey(0)