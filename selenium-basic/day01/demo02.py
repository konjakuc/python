# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://home.baidu.com/contact.html")
page_source = driver.page_source
emails = re.findall(r'[\w]+@\w+\.\w+', page_source)
for email in set(emails):
    print(email)
driver.close()