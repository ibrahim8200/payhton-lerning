import cv2
import numpy as np
import requests

url = "http://192.168.1.100:8080//shot.jpg"


name = "video1.avi"
cadoc = cv2.VideoWriter_fourcc('W ','M', 'V', '2')
fremRate=30
boyut = (640 , 480)

videoFileOutput = cv2.VideoWriter(name, cadoc, fremRate, boyut)
cascade = cv2.CascadeClassifier("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\xml_dosyalari\\frontalface.xml.xml")

while True:
    img_vid = requests.get(url)
    vid_arr = np.array(bytearray(img_vid.content), dtype=np.uint8)

    img = cv2.imdecode(vid_arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (640, 480))

    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(grey, 1.5, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), ((x+w), (y+h)), (255, 0, 0), 2)

    videoFileOutput.write(1)
    cv2.imshow("Telefon", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
videoFileOutput.release()