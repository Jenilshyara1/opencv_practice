import cv2 

cap = cv2.VideoCapture('dog.mp4')

img = cv2.imread('dog.jpg')
print(img.shape)
# shape of image= (height,width,channels)
def rescale(frame,scale=0.50):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    print(height)
    print(width)
    dimension = (width,height)
    return cv2.resize(frame,dimension,interpolation=cv2.INTER_AREA)

while True:
    ret, frame = cap.read()
    resized_frame = rescale(frame)
    cv2.imshow('dog',resized_frame)
    if cv2.waitKey(29) & 0xFF==ord('d'):
        break
cap.release()
cv2.destroyAllWindows()
