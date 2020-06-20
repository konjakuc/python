# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.toutiao.com")
spanList = driver.find_elements_by_xpath("//a/span")
for span in spanList:
    if span.text == "科技":
        span.click()
        break
allTitle = driver.find_elements_by_xpath("//a[@class='link title']")
for title in allTitle:
    print(title.text)
