


from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException

browser = webdriver.Chrome()

try:
    browser.get('www.baidu.com')
except TimeoutException:
    print('time out ')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('no element')
finally:
    browser.close()


'-------------------------------------'
































