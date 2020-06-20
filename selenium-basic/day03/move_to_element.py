# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://www.baidu.com")

ac = ActionChains(driver)
ac.move_to_element(driver.find_element_by_css_selector('[name="tj_briicon"]')).perform()
