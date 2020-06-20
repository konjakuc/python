# -*- coding: utf-8 -*-

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///D:/selenium_pages/alert.html")
promptBtn = driver.find_element_by_id("b3")
time.sleep(1)
promptBtn.click()
alertEle = driver.switch_to.alert
print(alertEle.text)
time.sleep(1)
alertEle.send_keys("selenium")
alertEle.accept()
time.sleep(2)
promptBtn.click()
time.sleep(1)
alertEle.dismiss()
time.sleep(2)
driver.quit()