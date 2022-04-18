import cv2
import numpy as np
import time
import face_recognition
def increaseBirghtness(image, value =30):
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    h,s,v=cv2.split(hsv)
    lim = 255 - value
    v[v>lim] = 255
    v[v<=lim] +=value
    final_hsv = cv2.merge((h,s,v))
    img= cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
video = cv2.VideoCapture(0)
count = 0
l =[]
while True:
    ret, frame = video.read()
    frame = increaseBirghtness(frame, value=100)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break