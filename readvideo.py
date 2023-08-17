import cv2 

cap = cv2.VideoCapture('dog.mp4')

# digit = cap.get(cv2.CAP_PROP_FRAME_COUNT)
# print(digit)

while True:
    istrue,frame =  cap.read()

    cv2.imshow('video',frame)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

cap.release()
cv2.destroyAllWindows()