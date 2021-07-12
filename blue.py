import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True :
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)
    hsv_frm = cv2.cvtColor(frm, cv2.COLOR_BGR2HSV)

    red_lower = np.array([0,50,20], np.uint8)
    red_upper = np.array([5,255,255], np.uint8)
    redd = cv2.inRange(hsv_frm, red_lower, red_upper)
    red = cv2.bitwise_and(frm, frm, mask=redd)

    blu_lower = np.array([94, 80, 2], np.uint8)
    blu_upper = np.array([120,255,255], np.uint8)
    bluu = cv2.inRange(hsv_frm, blu_lower, blu_upper)
    blu = cv2.bitwise_and(frm, frm, mask=bluu)

    cv2.imshow("blue", blu)
    cv2.imshow("orginal", frm)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
