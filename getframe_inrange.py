import cv2 

cap = cv2.VideoCapture('dog.mp4')

start_frame = 50
stop_frame = 100
step_frame = 10

for i in range(start_frame,stop_frame,step_frame):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)

    ret, frame = cap.read()

    if ret:
        cv2.imwrite(f'dog{i}.jpg',frame)