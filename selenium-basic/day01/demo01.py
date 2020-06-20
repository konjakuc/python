# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
allA = driver.find_elements_by_tag_name("a")
for a in allA:
    print(a.text)
driver.close()