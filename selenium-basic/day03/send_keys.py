# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://www.baidu.com")

logo = driver.find_element_by_css_selector("#lg > img.index-logo-src")
actions = ActionChains(driver)
actions.context_click(logo).send_keys(Keys.ARROW_DOWN, Keys.ENTER).perform()
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.quit()