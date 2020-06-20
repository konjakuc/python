# -*- coding: utf-8 -*-

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://tieba.baidu.com/")
targetEle = driver.find_element_by_link_text("地区")
driver.execute_script("arguments[0].scrollIntoView();", targetEle)  # arguments[0] => targetEle

# 移动到元素的底端与当前窗口的底部对齐：
# dr.execute_script("arguments[0].scrollIntoView(false);", target)
# 移动到元素的顶端与当前窗口的顶部对齐：
# dr.execute_script("arguments[0].scrollIntoView();", target)
# 移动到页面底部：
# dr.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# 移动到页面顶部：
# dr.execute_script("window.scrollTo(0, 0)")
try:
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 0)")
finally:
    time.sleep(3)
    driver.quit()