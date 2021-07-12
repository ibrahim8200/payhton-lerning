import cv2

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\xml_dosyalari\\frontalface.xml.xml")

while 1:
    ret, frem = cap.read()
    frem = cv2.flip(frem,1)
    if ret == 0:
        break
    grey = cv2.cvtColor(frem, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(grey, 1.5, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frem, (x, y), ((x+w), (y+h)), (255, 0, 0), 2)
    if cv2.waitKey(10) == 27:
        break
    cv2.imshow("faces", frem)
cap.release()
cv2.destroyAllWindows()
