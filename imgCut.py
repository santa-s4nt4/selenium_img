from PIL import Image
from selenium import webdriver
import io
from urllib import request

import cv2
import numpy as np
import glob
import sys, os

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

in_jpg = "./img/"
out_jpg = "./imgCut/"

def get_file(dir_path):
        filenames = os.listdir(dir_path)
        return filenames

pic = get_file(in_jpg)

for i in pic:
        image_gs = cv2.imread(in_jpg + i)
        
        cascade = cv2.CascadeClassifier("C:\\Users\\santa\\.virtualenvs\\selenium_img--xVpDsKx\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
        
        face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
        
        no = 1;

        for rect in face_list:
                x = rect[0]
                y = rect[1]
                width = rect[2]
                height = rect[3]
                dst = image_gs[y: y + height, x: x + width]
                save_path = out_jpg + '/' + 'out_(' + str(i) + ')' + str(no) + '.jpg'
                
                a = cv2.imwrite(save_path, dst)
                print(no)
                no += 1