import cv2
import numpy as np
flash = np.ones((1080, 1920), np.uint8) *255
camera = cv2.VideoCapture(0)
while True:
    # input("press to capture camera")
    ret ,frame =camera.read();
    cv2.namedWindow("flash", cv2.WINDOW_NORMAL)
    # cv2.setWindowProperty("flash", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("flash", flash)
    cv2.imshow("f",frame)
    cv2.waitKey(1) & 0xFF == ord('q')
    return_value, image = camera.read()
# cv2.destroyWindow("flash")
