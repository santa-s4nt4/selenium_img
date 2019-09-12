from PIL import Image
from selenium import webdriver
import io
from urllib import request

browser = webdriver.Chrome(executable_path='C:\\Users\\santa\\chromedriver_win32\\chromedriver.exe')
browser.get('https://santa-sukitoku.github.io/santa-portfolio/')
elem = browser.find_element_by_class_name('module')
elem = elem.find_element_by_tag_name('img')
url = elem.get_attribute('src')
f = io.BytesIO(request.urlopen(url).read())
img = Image.open(f)
img.save('./img/img01.jpg')