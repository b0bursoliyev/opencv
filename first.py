import cv2
import numpy as np
import os


img_path = os.path.join('.','images','bird.jpg')

img = cv2.imread(img_path)

cv2.imwrite(os.path.join('.','images','bird_out.jpg'),img)
