import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
element = driver.find_element_by_id("kw")
element.send_keys("alphacoding\n")

time.sleep(3)
alla = driver.find_elements_by_tag_name("a")


select = Select(driver.find_element_by_id())
# 创建实例
select.select_by_value()
# 选择xx
select.deselect_all()
# 全部取消

ac = ActionChains(driver)
ac.move_to_element().perform()