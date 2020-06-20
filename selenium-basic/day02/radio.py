# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///D:/selenium_pages/form_web_element.html")

currntTcher = driver.find_element_by_css_selector("#s_radio input[checked='checked']")
print(currntTcher.get_attribute("value"))

driver.find_element_by_css_selector("#s_radio input[value='小雷老师']").click()