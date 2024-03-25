import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('.','images','whiteboard.jpg'))
# line
print(img.shape)
cv2.line(img,(100,100),(850,850),(255,0,0),3)
# rectangle
cv2.rectangle(img,(100, 100), (400, 400), (0,0,255),3)
# circle
cv2.circle(img,(600,200),100,(0, 255, 0),5)
# text
cv2.putText(img,'the text',(300,200),cv2.FONT_HERSHEY_COMPLEX,2,(150,200,0), 3)
cv2.imshow('img',img)
cv2.waitKey(0)