import os
import cv2

img = cv2.imread(os.path.join('.','images','freelancer.png'))
img = cv2.resize(img,(800,412))
k_size = 9
img_blur = cv2.blur(img,(k_size,k_size))
g_blur = cv2.GaussianBlur(img,(k_size,k_size),5)
median_blur = cv2.medianBlur(img,k_size)

cv2.imshow('freelancer',img)
cv2.imshow('img_blur',img_blur)
cv2.imshow('g_blur',g_blur)
cv2.imshow('median_blur',median_blur)
cv2.waitKey(0)
