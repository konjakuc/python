# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver


def open_blog():
    # 打开浏览器
    driver = webdriver.Chrome()
    # 最大化
    driver.maximize_window()
    # 访问地址
    driver.get("")
    # 读取博客列表
    articles = driver.find_element_by_xpath("//div[@class='article-list']")
    item_list = articles.find_elements_by_class_name("article-item-box")
    print("len:", len(item_list))
    for i in range(len(item_list)):
        item = articles.find_element_by_xpath("//div[" + str(i+1) + "]/h4/a")
        print(item.text)
        item.click()

    time.sleep(1)
    driver.quit()


if __name__ == "__main__":
    for i in range(10):
        print(i)
        open_blog()
        time.sleep(10)

