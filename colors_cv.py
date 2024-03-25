import cv2
import os

img_path = os.path.join('.','images','bird.jpg')
img = cv2.imread(img_path)

img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2XYZ)

cv2.imshow(winname='img_rgb',mat=img_rgb)
cv2.imshow(winname='img',mat=img)
cv2.waitKey(0)
cv2.destroyAllWindows()
