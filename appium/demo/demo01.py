# -*- coding: utf-8 -*-

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from common.data import command_executor, desired_caps


with webdriver.Remote(command_executor, desired_caps) as driver:
    driver.implicitly_wait(5)

    # 输入用户名
    driver.find_element_by_id('com.example.todolist:id/nameET').send_keys(1)
    # 输入密码
    driver.find_element_by_id('com.example.todolist:id/passwordET').send_keys(1)
    # 点击登录
    driver.find_element_by_id('com.example.todolist:id/loginBtn').click()

    # 点击添加按钮
    driver.find_element_by_id('com.example.todolist:id/action_new').click()
    # 添加内容
    driver.find_element_by_id('com.example.todolist:id/toDoItemDetailET').send_keys('111')
    # 点击保存
    driver.find_element_by_id('com.example.todolist:id/saveBtn').click()

    # 长按
    detail_ele = driver.find_element_by_id('com.example.todolist:id/toDoItemDetailTv')
    TouchAction(driver).long_press(detail_ele).perform()

    # 点击删除按钮
    delete_button = driver.find_element_by_android_uiautomator('text("删除")')
    TouchAction(driver).tap(delete_button).perform()

    # 点击确定按钮
    ok_button = driver.find_element_by_android_uiautomator('text("确定")')
    TouchAction(driver).tap(ok_button).perform()

    time.sleep(5)