# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("file:///D:/selenium_pages/form_web_element.html")
selectEle = Select(driver.find_element_by_id("ss_single"))
try:
    assert len(selectEle.options) == 3
except AssertionError:
    print("Test failed! The number of options in the select box is not 3.")
else:
    print("Test pass! The number of options in the select box is 3.")
finally:
    time.sleep(3)
    driver.quit()
