import cv2
import os
import numpy as np
img = cv2.imread(os.path.join('.','images','Camavinga.jpg'))

imge_edge = cv2.Canny(img,50,200)

img_edge_d = cv2.dilate(imge_edge,np.zeros((11, 11),dtype=np.uint8))

cv2.imshow('Camavinga',img)
cv2.imshow('img_edge_d',img_edge_d)
cv2.imshow('imge_edge',imge_edge)

cv2.waitKey(0)