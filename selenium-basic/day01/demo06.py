# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://github.com/login")

testName = "testusername"
testPswd = "testpassword"
# 输入用户名
usName_box = driver.find_element_by_id("login_field")
usName_box.send_keys(testName)

# 输入密码
pswd_box = driver.find_element_by_id("password")
pswd_box.send_keys(testPswd)

# 点击登录按钮
signIn_button = driver.find_element_by_css_selector(".btn")
signIn_button.click()

# 判断用户
usMeta = driver.find_element_by_css_selector('head > meta[name="user-login"]')
assert usMeta.get_attribute("content") == testName

# 点击菜单
headerMenu = driver.find_element_by_css_selector("span.dropdown-caret:nth-child(3)")
headerMenu.click()

# 退出账号并关闭浏览器
signOut_button = driver.find_element_by_css_selector(".dropdown-signout")
signOut_button.click()
driver.quit()

