# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options


@pytest.fixture()
def driver(driver_type="chrome"):
    if driver_type == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif driver_type == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif driver_type == "chrome-headless":
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    elif driver_type == "firefox-headless":
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise NameError("driver驱动类型定义错误")

    yield driver
    driver.quit()
    print("test end!")
