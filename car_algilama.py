import cv2

vid = cv2.VideoCapture("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\video\\car.mp4")
casbody = cv2.CascadeClassifier("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\xml_dosyalari\\car.xml")


while 1:
    ret, frem = vid.read()
    frem = cv2.resize(frem, (640,480))
    if ret == 0:
        break
    gray = cv2.cvtColor(frem, cv2.COLOR_BGR2GRAY)
    body = casbody.detectMultiScale(gray, 2.5, 1)

    for (x, y, w, h) in body:
        cv2.rectangle(frem, (x, y),(x+w, y+h), (0,255,0), 2)
    cv2.imshow("body", frem)
    if cv2.waitKey(20) == 27:
        break
cv2.destroyAllWindows()