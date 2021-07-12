import cv2

vid = cv2.VideoCapture(0)
cassmile = cv2.CascadeClassifier("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\xml_dosyalari\\smile.xml")
casface = cv2.CascadeClassifier("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\xml_dosyalari\\yuz.xml")

while 1:
    ret, frem = vid.read()
    frem = cv2.flip(frem, 1)
    frem = cv2.resize(frem, (640, 480))
    if ret == 0:
        break
    gray = cv2.cvtColor(frem, cv2.COLOR_BGR2GRAY)
    yuz = casface.detectMultiScale(gray)

    for (x, y, w, h) in yuz:
        pass
        frem2 = frem[y:y+h, x:x+w]
        gray2 = gray[y:y+h, x:x+w]
        smile = cassmile.detectMultiScale(gray2, 2.8, 6)
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(frem2, (sx,sy), (sx+sw, sy+sh), (0, 255,0), 1)
    cv2.imshow("smile", frem)
    if cv2.waitKey(1) == 27:
        break
vid.release()
cv2.destroyAllWindows()