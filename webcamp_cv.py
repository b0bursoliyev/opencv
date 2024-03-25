import os
import cv2

cam = cv2.VideoCapture(0)

while True:
  ret,frame = cam.read()
  frame = cv2.resize(frame,(1080,720))
  frame = cv2.Canny(frame,100,200)

  cv2.imshow('frame',frame)

  if cv2.waitKey(40) & 0xFF==ord('q'):
    break


cam.release()
cv2.destroyAllWindows()