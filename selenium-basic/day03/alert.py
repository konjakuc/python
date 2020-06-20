# -*- coding: utf-8 -*-

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///D:/selenium_pages/alert.html")
time.sleep(1)
driver.find_element_by_id("b1").click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
driver.quit()