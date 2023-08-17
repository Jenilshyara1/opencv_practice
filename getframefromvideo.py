import cv2 

cap = cv2.VideoCapture('dog.mp4')

frame_num  = 200

cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)     #  sets the position of the video to the specified frame_num

ret , frame = cap.read()

if ret:
    cv2.imwrite('dog.jpg',frame)