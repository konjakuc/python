# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

# 请在Chrome方法中，传入驱动的字符串路径
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
assert "百度" in driver.title

