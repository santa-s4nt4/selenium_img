from PIL import Image
from selenium import webdriver
import io
from urllib import request

browser = webdriver.Chrome(executable_path='C:\\Users\\santa\\chromedriver_win32\\chromedriver.exe')
browser.get('https://twitter.com/hashtag/sense_connect?src=hashtag_click')
#elems = browser.find_elements_by_class_name('AdaptiveMedia-singlePhoto')
elems = browser.find_elements_by_class_name('AdaptiveMedia-photoContainer')
for index, elem in enumerate(elems):
        elem = elem.find_element_by_tag_name('img')
        url = elem.get_attribute('src')
        f = io.BytesIO(request.urlopen(url).read())
        img = Image.open(f)
        img.save('./sense/img{}.jpg'.format(index))
        
browser.quit()