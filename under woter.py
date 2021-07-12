
import cv2
import numpy as np

vid = cv2.VideoCapture("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\video\\underw.mp4")
while 1:
    ret, frem = vid.read()
    frem = cv2.resize(frem, (640, 480))
   # frem = cv2.blur(frem, (5, 5))

    Hsv = cv2.cvtColor(frem , cv2.COLOR_BGR2HSV)

    red_lower = np.array([0, 50, 20], np.uint8)
    red_upper = np.array([5, 255, 255], np.uint8)

    mask = cv2.inRange(Hsv, red_lower, red_upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = lambda x: cv2.contourArea(x), reverse=False)


    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radios) = cv2.minEnclosingCircle(c)


    for cnt in contours:
        area = cv2.contourArea(cnt)
        if  area > 2000  :
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(frem, (x, y), (x + w, y + h), (0, 255, 0), 2)
            mask1 =frem[y: y+h , x:x+w]
            width, height = mask1.shape[:2]
            cv2.circle(mask1, ( int(height/2),int(width/2) ), 5, (0, 255, 0), -1)
            print(area)
            break


    cv2.imshow("video", frem)
    cv2.imshow("Red", mask)


    if cv2.waitKey(10) == 27:
        break
vid.release()
cv2.destroyAllWindows()
