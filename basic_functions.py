import cv2

img = cv2.imread('dog.jpg')
cv2.imshow('original',img)


# convert to grayscale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',img_gray)

# blur the image
blur = cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow('blur',blur)

# edge cascade
edge = cv2.Canny(img,threshold1=100,threshold2=100)
cv2.imshow('edges',edge)

# resize 
resized = cv2.resize(img,(800,500),interpolation=cv2.INTER_AREA)
cv2.imshow('resize',resized)

# cropping image
crop = img[:200,:500]
cv2.imshow('crop',crop)

cv2.waitKey(0)


