from PIL import Image
from selenium import webdriver
import io
from urllib import request

import cv2
print(cv2.__version__)

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
        img.save('./imgCut/img{}.jpg'.format(index))