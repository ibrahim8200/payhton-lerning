import cv2
import numpy as np
from scipy import constants
import requests

vid = cv2.VideoCapture(0)
url = "http://172.31.1.241:8080//shot.jpg"


# ---- videokayid etme ------#
name = "video1.avi"
cadoc = cv2.VideoWriter_fourcc('W ','M', 'V', '2')
fremRate=30
boyut = (640 , 480)
videoFileOutput = cv2.VideoWriter(name , cadoc, fremRate, boyut)

# ---------------------------#
x = 1200

#vid = cv2.VideoCapture(0)
while 1:
    img_vid = requests.get(url)
    vid_arr = np.array(bytearray(img_vid.content), dtype=np.uint8)
    img = cv2.imdecode(vid_arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (640, 480))
    frem = img

    #_, frem = vid.read()

    Hsv = cv2.cvtColor(frem, cv2.COLOR_BGR2HSV)

    red_lower = np.array([170, 50, 50])
    red_upper = np.array([180, 255, 255])

    mask = cv2.inRange(Hsv, red_lower,
                       red_upper)  # HSV Formatina dönen görüntünün bizim belirtiğimiz sınırları içerisinde olanları belirliyor

    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, mask.shape[0] / 4, param1=200, param2=15, minRadius=35,maxRadius=89)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Hedefin Adresi bolma
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=False)  # buyuktan kucuğa sırala

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radios) = cv2.minEnclosingCircle(c)


        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                cv2.circle(frem, (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv2.circle(frem, (i[0], i[1]), 5, (0, 255, 0), -1)


    cv2.imshow("video", frem)
    cv2.imshow("Red", mask)

    if cv2.waitKey(1) == 27:
        break
vid.release()
cv2.destroyAllWindows()
