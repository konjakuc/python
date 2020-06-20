# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
driver = webdriver.Chrome ()
driver.get("http://py101.net/login?from=%2F")
allImg = driver.find_elements_by_tag_name("img")
for img in allImg:
    print(img.get_attribute("src"))
driver.close()