# -*- coding: utf-8 -*-

import time
from selenium import webdriver


def crawlBookTitle(driver, cssSelector):
    books = driver.find_elements_by_css_selector(cssSelector)
    for book in books:
        print(book.text)


def main(driver):
    driver.maximize_window()
    driver.get("https://book.douban.com/")
    driver.implicitly_wait(3)
    driver.find_element_by_link_text("豆瓣书店").click()
    while True:
        crawlBookTitle(driver, ".book-brief h3")
        lastBtn = driver.find_elements_by_css_selector(".item")[-1]
        if lastBtn.text != "后页»":
            break
        lastBtn.click()


driver = webdriver.Chrome()
try:
    main(driver)
finally:
    time.sleep(3)
    driver.quit()
