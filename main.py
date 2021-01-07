import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# 实例化浏览器  打开谷歌浏览器
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
# 全屏方式打开
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(5)

# list01 = _driver.find_elements_by_css_selector('#hotsearch-content-wrapper li a span:nth-child(1)')
# a = 1
# while a == 1:
#     for i in list01:
#         if i.text == '20':
#             i.click()
#             a = 2
#     _driver.find_element_by_id('hotsearch-refresh-btn').click()

list02 = driver.find_elements_by_css_selector('#hotsearch-content-wrapper li a span:nth-child(3)')
a = 1
while a == 1:
    for i in list02:
        if i.text == '新':
            i.click()
           # a = 2
    driver.find_element_by_id('hotsearch-refresh-btn').click()


