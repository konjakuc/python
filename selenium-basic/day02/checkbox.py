# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///D:/selenium_pages/form_web_element.html")

checkedTchers = driver.find_elements_by_css_selector("#s_checkbox input[checked='checked']")
for teacher in checkedTchers:
    teacher.click()

driver.find_element_by_css_selector("#s_checkbox input[value='小雷老师']").click()