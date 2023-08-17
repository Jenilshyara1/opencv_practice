import cv2 

cap = cv2.VideoCapture('dog.mp4')

#time[sec] = frame / FPS
sec = 11
fps = cap.get(cv2.CAP_PROP_FPS)

cap.set(cv2.CAP_PROP_POS_FRAMES, round(fps * sec))

ret, frame = cap.read()

if ret:
    cv2.imwrite('dog.jpg', frame)