import cv2 
import numpy as np
img = cv2.imread('dog.jpg',cv2.IMREAD_GRAYSCALE)


th,dst = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
print(th)
cv2.imshow('thresold',dst)
cv2.waitKey(0)