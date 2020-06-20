# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
try:
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.LINK_TEXT, "新闻")))
    driver.find_element(By.LINK_TEXT, "新闻").click()
    print(driver.title)
finally:
    driver.quit()