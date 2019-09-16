import cv2
import numpy as np

HAAR_FILE = "C:\\Users\\santa\\.virtualenvs\\selenium_img--xVpDsKx\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)

image_picture = "./img/img0.jpg"
imgCut = cv2.imread(image_picture)

imgCut_g = cv2.imread(image_picture, 0)

face = cascade.detectMultiScale(imgCut_g)

print(face)

for x,y,w,h in face:
    face_cut = imgCut[y:y+h, x:x+w]
        
cv2.imwrite('./imgCut/imgCut.jpg', face_cut)