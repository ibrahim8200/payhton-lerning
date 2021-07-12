import cv2  # opencv kütüphanesi dahil etme
import numpy as np  # Numpy kütüphanesi dahil etme

vid = cv2.VideoCapture(0) #Kamera aktif hale gelir
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while 1: #aşağıdaki işlemleri sonsuza tekrarlansın
    ret, frem = vid.read() #Kamerdan gelen görüntü frem değişkene aktarılır
    frem = cv2.flip(frem, 1) # Fremi 180 derece cevir

    if ret:

        #frem = cv2.blur(frem , (9, 9))
        Hsv  = cv2.cvtColor(frem , cv2.COLOR_BGR2HSV) #BGR formatında gelen görüntüer HSV formatına çevrilir.

        red_lower = np.array([170, 50, 50]) # kırmızı rengın aralığı
        red_upper = np.array([180, 255, 255]) # kırmızı rengın aralığı

        mask = cv2.inRange(Hsv, red_lower, red_upper) #HSV Formatina dönen görüntünün bizim belirtiğimiz sınırları içerisinde olanları belirliyor
        #mask = cv2.erode(mask, None, iterations=2) #Bizim rengleri işaretliyor
        #mask = cv2.dilate(mask, None, iterations=2) #Bizim Renlerimizin genişliği alıyor

        contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Hedefin Adresi bolma
        contours = sorted(contours, key = lambda x: cv2.contourArea(x), reverse=False) # buyuktan kucuğa sırala

        for cnt in contours:

            epsilon = 0.01 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            #cv2.drawContours(frem, [approx], 0, (0), 3)
            # Position for writing text
            x2, y2 = approx[0][0]

            if len(approx) == 2:
                cv2.putText(frem, "Ucgen ", (x2, y2), cv2.FONT_HERSHEY_COMPLEX, 3, 3, 3)


            #area = cv2.contourArea(cnt)
            #if area > 250: # Alan 250den büyük ise aşagıdakileri yap
            #    (x, y, w, h) = cv2.boundingRect(cnt) # hedfin alani ve adresi diğişken içinde saklar
            #    cv2.rectangle(frem, (x, y), (x + w, y + h), (0, 255, 0), 2) # Hedefin atrafinda kara çizme
            #
            #    frem1 = frem[y:y+h , x:x+w]
            #
            #    x_kor =str(x+w/2) # x Kordinatı sakla
            #    y_kor = str(y+h/2) # y Kordinatı sakla
            #
            #    cv2.circle(frem, (int(x+w/2) ,int(y+h/2) ), 5, (0, 255, 0), -1) # istenilen kordinata çember oluştur
            #
            #    print("x Kordinatı : " + x_kor ) # Rengin bulundugu X Kordinati
            #    print("Y Kordinatı : " + y_kor ) # Rengin bulundugu Y Kordinati
            #break

        cv2.imshow("frem", frem)  # fremleri göster
        cv2.imshow("mask", mask)  #kırmızı rengin algılaması göster


        if cv2.waitKey(1) == 27:  # ESC basinca kapat
            break

vid.release()
cv2.destroyAllWindows()
