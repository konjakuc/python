# -*- coding: utf-8 -*-

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///D:/selenium_pages/alert.html")
confirmBtn = driver.find_element_by_id("b2")
time.sleep(1)
confirmBtn.click()
driver.switch_to.alert.accept()
time.sleep(2)
confirmBtn.click()
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.quit()