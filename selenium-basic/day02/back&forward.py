# -*- coding: utf-8 -*-

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(2)
driver.find_element_by_link_text("新闻").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.quit()
