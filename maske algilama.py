import cv2

vid = cv2.VideoCapture(0)

casagiz = cv2.CascadeClassifier("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\xml_dosyalari\\agiz.xml")
casface = cv2.CascadeClassifier("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\xml_dosyalari\\face1.xml")

face_yok = "Kimse Yok"
maske_var = "Maske Taktigin icin Tesekkur ederim"
maske_yok = "Lutfen Maskeni Tak"

while 1:
    ret, frem = vid.read()
    frem = cv2.flip(frem, 1)
    frem = cv2.resize(frem, (640,480))

    if ret == 0:
        break

    gray = cv2.cvtColor(frem, cv2.COLOR_BGR2GRAY)

    faces = casface.detectMultiScale(gray, 1.1, 4)

    _, thers = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

    face_bw = casface.detectMultiScale(thers, 1.1, 4)

    if len(faces) == 0 and len(face_bw) == 0:
            cv2.putText(frem, face_yok, (30, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

    else:
        for (x, y, w, h) in faces:
            img = frem[x:x + w, y:y + h]
            gray1 = gray[x:x + w, y:y + h]

            cv2.rectangle(frem, (x, y), (x + w, y + h), (0, 255, 0), 1)
        agiz = casagiz.detectMultiScale(gray, 1.5, 5)

        if len(agiz) == 0:
                cv2.putText(frem, maske_var, (10, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))

        else:
            cv2.putText(frem, maske_yok, (30, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 250))

    cv2.imshow("maske", frem)

    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()
