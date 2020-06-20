# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///D:/selenium_pages/iframe_sample.html")
driver.switch_to.frame("frame1")
plants = driver.find_elements_by_css_selector(".plant span")

for plant in plants:
    print(plant.text)