# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

input_box = driver.find_element_by_id("kw")
input_box.send_keys("selenium")

baidu_button = driver.find_element_by_id("su")
baidu_button.click()
