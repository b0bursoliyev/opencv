import cv2
import os

img = cv2.imread(os.path.join('.','images','lots_of_birds3.png'))

img = cv2.resize(img,(720,680))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img_gray,250,300,cv2.THRESH_BINARY_INV)

countrs,hierarcy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in countrs:
  if cv2.contourArea(cnt)>200:
    # cv2.drawContours(img,cnv,-1,(255, 0, 2),-1)
    x1,y1,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x1,y1), (x1+w,y1+h), (255,0,0),1)
cv2.imshow('img',img)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
