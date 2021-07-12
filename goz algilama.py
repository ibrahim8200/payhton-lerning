import cv2

cap = cv2.VideoCapture(0)

casyuz = cv2.CascadeClassifier("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\xml_dosyalari\\yuz.xml")
casgoz = cv2.CascadeClassifier("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\xml_dosyalari\\goz.xml")
while 1:
    ret, frem = cap.read()
    if ret == 0:
        break
    frem = cv2.flip(frem, 1)

    gray = cv2.cvtColor(frem, cv2.COLOR_BGR2GRAY)

    yuz = casyuz.detectMultiScale(gray, 1.5, 4)

    for (x, y, w, h) in yuz:
        cv2.rectangle(frem, (x, y), (x+w, y+h), (0,100,200), 2)
        img2 = frem[y:y+h, x:x+w]
        gray2 = gray[y:y+h, x:x+w]
        goz = casgoz.detectMultiScale(gray2)

        for (gx, gy, gw, gh) in goz:
            cv2.rectangle(img2, (gx, gy), (gx+gw, gy+gh), (0,100,200), 2)

    cv2.imshow("goz algilama", frem)

    if cv2.waitKey(30) == 27:
        break
cap.release()
cv2.destroyAllWindows()


