import cv2
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
blank1 = np.zeros((500,500,3),dtype='uint8')
blank2 = np.zeros((500,500,3),dtype='uint8')

# draw a rectangle
cv2.rectangle(blank,(100,100),(200,200),(255,0,0),thickness=2)
cv2.rectangle(blank,(300,100),(400,200),(255,0,0),thickness=2)

# draw a line
cv2.line(blank,(150,350),(350,350),(255,0,0),thickness=2)

cv2.imshow('box',blank)

# draw a circle
cv2.circle(blank1,(250,250),radius=100,color=(0,0,255),thickness=-1)
cv2.imshow('circle',blank1)

# write text
cv2.putText(blank2,'Helllo Jenil',(100,250),fontFace=cv2.FONT_ITALIC,fontScale=1,color=(0,255,0 ),thickness=2)
cv2.imshow('text',blank2)

cv2.waitKey(0)