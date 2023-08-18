import cv2
img  = cv2.imread('dog.jpg')

# rotation

rotate = cv2.rotate(img,rotateCode=cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('rotate90',rotate)

# rotation with angle
height,width = img.shape[0],img.shape[1]
center = (img.shape[1]//2,img.shape[0]//2)
print(center)
def rotation(img,angle):
    rotation_matrix = cv2.getRotationMatrix2D(center,angle,scale=0.25)
    rotated = cv2.warpAffine(img,rotation_matrix,(width,height))
    return rotated

rotated = rotation(img,90)
cv2.imshow('rotate45',rotated)

# flipping 
# 0 = vertical
# 1 = horizontal
# -1 = vertical and horizontal
flip = cv2.flip(img,0)
cv2.imshow('flip',flip)

cv2.waitKey(0)