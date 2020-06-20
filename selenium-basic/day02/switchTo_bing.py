# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///D:/selenium_pages/swtich_window_sample.html")
driver.find_element_by_css_selector("a[href='http://www.bing.com']").click()
driver.switch_to.window(driver.window_handles[1])
print(driver.title)