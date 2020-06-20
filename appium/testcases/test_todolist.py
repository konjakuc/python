# -*- coding: utf-8 -*-

import allure
from appium.webdriver.common.touch_action import TouchAction
from common.logger import getLogger

logger = getLogger('todolist')


@allure.feature('待办事项')
class Test_todolist(object):

    @allure.story('登录')
    def test_login(self, driver):
        # 输入用户名
        driver.find_element_by_id('com.example.todolist:id/nameET').send_keys(1)
        # 输入密码
        driver.find_element_by_id('com.example.todolist:id/passwordET').send_keys(1)
        # 点击登录
        driver.find_element_by_id('com.example.todolist:id/loginBtn').click()

    @allure.story('添加待办')
    def test_addDetail(self, driver):
        # 点击添加按钮
        driver.find_element_by_id('com.example.todolist:id/action_new').click()
        # 添加内容
        driver.find_element_by_id('com.example.todolist:id/toDoItemDetailET').send_keys('1')
        # 点击保存
        driver.find_element_by_id('com.example.todolist:id/saveBtn').click()

    @allure.story('删除待办')
    def test_deleteDetail(self, driver):
        # 长按
        detail_ele = driver.find_element_by_id('com.example.todolist:id/toDoItemDetailTv')
        TouchAction(driver).long_press(detail_ele).perform()

        # 点击删除按钮
        # find_element_by_android_uiautomator('new UiSelector().text("删除")')
        delete_button = driver.find_element_by_android_uiautomator('text("删除")')
        TouchAction(driver).tap(delete_button).perform()

        # 点击确定按钮
        ok_button = driver.find_element_by_android_uiautomator('text("确定")')
        TouchAction(driver).tap(ok_button).perform()
