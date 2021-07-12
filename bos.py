
import cv2
import numpy as np
from scipy import constants
x1 = 1200


vid = cv2.VideoCapture("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\video\\underw.mp4")
while 1:
    ret, frem = vid.read()
    frem = cv2.resize(frem, (640, 480))
    frem = cv2.blur(frem, (9, 9))

    Hsv = cv2.cvtColor(frem , cv2.COLOR_BGR2HSV)

    red_lower = np.array([0, 50, 20], np.uint8)
    red_upper = np.array([5, 255, 255], np.uint8)

    mask = cv2.inRange(Hsv, red_lower, red_upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:
            cv2.drawContours(treshold, [approx], 0, (0, 0, 0), 5)

            if len(approx) == 3:
                cv2.putText(treshold, "ucgen", (x, y), font, 1, (0, 0, 0))

            elif len(approx) == 4:
                cv2.putText(treshold, "Dortgen", (x, y-10), font, 1, (0, 0, 0))

            elif len(approx) == 5:
                cv2.putText(treshold, "besgen", (x+10, y), font, 1, (0, 0, 0))
            elif len(approx) == 6:
                cv2.putText(treshold, "Altigen", (x + 10, y), font, 1, (0, 0, 0))
            else:
                cv2.putText(treshold, "Daire", (x , y-60), font, 1, (0, 0, 0))

    cv2.imshow("img", frem)
    cv2.imshow("orginal", mask)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()