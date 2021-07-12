import cv2
import imutils as imutils
import numpy as np
import pytesseract

img = cv2.imread("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\img\\licence_plate.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_iyi = cv2.bilateralFilter(gray, 6, 250, 250)
img_iyi = cv2.Canny(gray_iyi, 50, 255)

contorus = cv2.findContours(img_iyi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(contorus)
cont = sorted(cont, key=cv2.contourArea, reverse=True)[:10]

for c in cont:
    epsilon = 0.018*cv2.arcLength(c, True)
    aprox= cv2.approxPolyDP(c, epsilon,True)
    if len(aprox) == 4:
        screen = aprox
        break


maskk = np.zeros(gray.shape, np.uint8)

new_img = cv2.drawContours(maskk, [screen], 0, (255, 255, 255), -1)
new_img = cv2.bitwise_and(img, img, mask=maskk)

(x,y) = np.where(maskk == (255))

(tx,ty) = (np.min(x), np.min(y))
(bx,by) = (np.max(x), np.max(y))

num = gray[ tx:bx+1, ty:by+1]

text = pytesseract.image_to_string(num, lang="eng")
print(text)
cv2.imshow("img", num)
cv2.imshow("img1", gray)
cv2.imshow("img2", gray_iyi)
cv2.imshow("img3", img_iyi)
cv2.imshow("img4", new_img)
cv2.imshow("img5", num)
cv2.imshow("img6", img)

cv2.waitKey(0)
cv2.destroyAllWindows()