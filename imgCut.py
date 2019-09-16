from PIL import Image
from selenium import webdriver
import io
from urllib import request

import cv2

print('type an instagram id') 
instagram = input('>> ')
print('id : ' + instagram)

browser = webdriver.Chrome(executable_path='C:\\Users\\santa\\chromedriver_win32\\chromedriver.exe')
browser.get('https://www.instagram.com/' + instagram)
elems = browser.find_elements_by_class_name('KL4Bh')
for index, elem in enumerate(elems):
        elem = elem.find_element_by_tag_name('img')
        url = elem.get_attribute('src')
        f = io.BytesIO(request.urlopen(url).read())
        img = Image.open(f)
        img.save('./img/img{}.jpg'.format(index))

HAAR_FILE = "C:\\Users\\santa\\.virtualenvs\\selenium_img--xVpDsKx\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)

image_picture = "./img/img0.jpg"
imgCut = cv2.imread(image_picture)

imgCut_g = cv2.imread(image_picture, 0)

face = cascade.detectMultiScale(imgCut_g)

print(face)

for x, y, w, h in face:
        face_cut = img[y: y + h, x: x + w]
        
cv2.imread('imgCut.jpg', face_cut)