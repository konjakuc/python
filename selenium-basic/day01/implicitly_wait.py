# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium\n")
driver.implicitly_wait(3)
print(driver.find_element_by_id(1).text)