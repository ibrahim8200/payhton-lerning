import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow("vido")

tracker = cv2.legacy.TrackerMOSSE_create()
suc, frem = cap.read()
frem = cv2.flip(frem, 1)
frem = cv2.resize(frem, (640, 480))
box = cv2.selectROI("vido", frem, False)
tracker.init(frem, box)

def drawBox(frem, box):
    x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    cv2.rectangle(frem, (x, y), ((x + w), (y + h)), (0, 20, 40), 2, 1)
    cv2.putText(frem, "Yakaladi", (70, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 250, 0), 2)

while 1:
    timer = cv2.getTickCount()
    suc,frem = cap.read()
    frem = cv2.flip(frem,1)
    frem = cv2.resize(frem, (640, 480))
    suc,box = tracker.update(frem)
    if suc:
      drawBox(frem,box)
    else:
        cv2.putText(frem, "Bulunmadi", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 250, 0), 2)

    FPS = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(frem, ("FPS :" + str(int(FPS))),(50,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,250,0),2)
    cv2.rectangle(frem,(45,40),(220,105),(0,255,0),2,2)

    print(cv2.EVENT_LBUTTONUP)
    cv2.imshow("vido", frem)
    key = cv2.waitKey(20)
    if key == 27:
       break
cap.release()
cv2.destroyWindow()
