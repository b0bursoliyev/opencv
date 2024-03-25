import cv2
import os

# img = cv2.imread(os.path.join('.','images','bear.jpg'),0)

# rate,threshold = cv2.threshold(img,70,255,cv2.THRESH_BINARY)

# cv2.imshow("Bear",img)
# cv2.imshow("threshold",threshold)

# cv2.waitKey(0)

img = cv2.imread(os.path.join('.','images','hardwrite.jpg'),0)
img = cv2.resize(img,(720,820))
rate,threshold = cv2.threshold(img,120,255,cv2.THRESH_BINARY)

adaptive_threshold = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,30)

cv2.imshow('hardwrite',img)
cv2.imshow('threshold',threshold)
cv2.imshow('adaptive_threshold',adaptive_threshold)
cv2.waitKey(0)