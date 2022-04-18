import cv2
import numpy as np
import time
import face_recognition
video = cv2.VideoCapture(0)
count = 0
l =[]
while True:
    ret, frame = video.read()
    # frame = increaseBirghtness(frame, value=100)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break