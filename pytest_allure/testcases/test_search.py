# -*- coding: utf-8 -*-

import time
import allure
from pages.baidu_page import BaiduPage

class TestBaduSearch():

    @allure.feature("用户功能")
    @allure.story("百度搜索")
    def test_baidu_search_case(self, driver):
        page = BaiduPage(driver)
        page.open()
        page.search("pytest")
        time.sleep(5)