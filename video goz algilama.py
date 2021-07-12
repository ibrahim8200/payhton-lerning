import cv2

vid = cv2.VideoCapture("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\video\\eye.mp4")

casyuz = cv2.CascadeClassifier("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\xml_dosyalari\\yuz.xml")

casgoz = cv2.CascadeClassifier("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\xml_dosyalari\\goz.xml")

while 1:
    ret, frem = vid.read()
    frem = cv2.flip(frem, 1)
    if ret == 0:
        break
    gray = cv2.cvtColor(frem, cv2.COLOR_BGR2GRAY)
    yuz = casyuz.detectMultiScale(gray, 1.4, 4)

    for (x, y, w, h) in yuz:
        img2 =frem[y:y+h, x:x+w]
        gray2 = gray[y:y+h, x:x+w]
        goz = casgoz.detectMultiScale(gray2)
        for (gx, gy, gw, gh) in goz:
            cv2.rectangle(img2, (gx, gy), ((gx+gw), (gy+gh)), (0, 255, 0), 2)
    cv2.imshow("goz", frem)
    if cv2.waitKey(20) == 27:
        break
vid.release()
cv2.destroyAllWindows()