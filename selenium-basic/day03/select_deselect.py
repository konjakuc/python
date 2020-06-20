# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("file:///D:/selenium_pages/form_web_element.html")
selectEle = Select(driver.find_element_by_id("ss_multi"))
selectEle.deselect_all()
selectEle.select_by_value("小雷老师")