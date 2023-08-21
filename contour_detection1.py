# A contour can be simply defined as a curve that joins a set of points enclosing an area having the same color or intensity. 
# cv2.RETR_EXTERNAL - retrieves only the extreme outer contours.
# cv2.RETR_LIST- retrieves all of the contours without establishing any hierarchical relationships.
# cv2.RETR_TREE - retrieves all of the contours and reconstructs a full hierarchy of nested contours.
# cv2.RETR_CCOMP - retrieves all of the contours and organizes them into a two-level hierarchy. At the top level, there are external boundaries of the components. At the second level, there are boundaries of the holes. If there is another contour inside a hole of a connected component, it is still put at the top level.

# Reference : https://learnopencv.com/contour-detection-using-opencv-python-c/

import cv2
import numpy as np


image = cv2.imread('Image.png',0) 

# Find all external contours in the image.
contours, hierarchy = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
new = cv2.imread('Image.png')
draw = cv2.drawContours(new,contours,-1,color=(0,255,0),thickness=3)
cv2.imshow('external contours',draw)


# Find all  contours in the image.
contours, hierarchy = cv2.findContours(image,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
new = cv2.imread('Image.png')
draw1 = cv2.drawContours(new,contours,-1,color=(0,255,0),thickness=3)
cv2.imshow('all contours',draw1)


cv2.waitKey(0)