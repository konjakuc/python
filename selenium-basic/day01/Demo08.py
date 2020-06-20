# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

WebDriverWait(driver, 3).until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[1])

help("assert")