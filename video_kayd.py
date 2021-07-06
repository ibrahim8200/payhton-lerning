import cv2
cap = cv2.VideoCapture(0 ,cv2.CAP_DSHOW)

name = "video.avi"
cadoc = cv2.VideoWriter_fourcc('W ','M', 'V', '2')
fremRate=30
boyut = (640 , 480)
videoFileOutput = cv2.VideoWriter(name , cadoc, fremRate, boyut )
while True:
    ret, frem = cap.read()
    frem = cv2.flip(frem, 1)
    videoFileOutput.write(frem)
    
    cv2.imshow("Webcam", frem)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
videoFileOutput.release()
