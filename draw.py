import cv2
import numpy as np

ashok = cv2.imread('0-4891_ashoka-chakra-png-transparent-image-ashok-chakra-logo.png')
blank = np.zeros((500,500,3),dtype='uint8')
blank2= np.zeros((500,500,3),dtype='uint8')
blank[:,:,0] = 0            # 0 for blue channel
blank[:,:,1] = 100          # 1 for green channel
blank[:,:,2] = 255          # 2 for red  channel
blank2[:,:,1] = 64
print(blank)
ashok = cv2.resize(ashok,(500,500),interpolation=cv2.INTER_AREA)
cv2.imshow('blue',blank)
cv2.imshow('green',ashok)
cv2.imshow('red',blank2)

cv2.waitKey(0) 

# arr = np.arange(4).reshape(2,2)
# print(arr[:])
# arr[:]=1,2
# print(arr[:])