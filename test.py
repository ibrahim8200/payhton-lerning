
import cv2
import numpy as np


vid = cv2.VideoCapture(0)
while 1:
    ret, frem = vid.read()
    frem = cv2.resize(frem, (640, 480))
    #frem = cv2.blur(frem, (9, 9))

    Hsv = cv2.cvtColor(frem , cv2.COLOR_BGR2HSV)

    red_lower = np.array([160,100,20])
    red_upper = np.array([179,255,255])


    mask = cv2.inRange(Hsv, red_lower, red_upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = lambda x: cv2.contourArea(x), reverse=False)


    try:
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            ((x, y), radios) = cv2.minEnclosingCircle(c)

            M = cv2.moments(c)  # Momenti hisapla ve M değşken içinde sakla
            Merkez = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))  # Merkez Adresi merkez değişken içersinde sakla

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area >950:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frem, (x, y), (x + w, y + h), (0, 255, 0), 2)
                mask1 =frem[y: y+h , x:x+w]
                width, height = mask1.shape[:2]
                cv2.circle(mask1, ( int(height/2),int(width/2) ), 5, (0, 255, 0), -1)
                break
    except:
        pass

    cv2.imshow("video", frem)
    cv2.imshow("Red", mask)


    if cv2.waitKey(10) == 27:
        break
vid.release()
cv2.destroyAllWindows()
