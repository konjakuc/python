# -*- coding: utf-8 -*-

import time
from selenium import webdriver


def simulateUserAccess(url, num, FPS=1):
    driver = webdriver.Chrome()
    driver.get(url)
    for i in range(num):
        time.sleep(FPS)
        driver.refresh()


simulateUserAccess("http://www.baidu.com", 5)
