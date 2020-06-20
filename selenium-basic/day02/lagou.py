# -*- coding: utf-8 -*-

import time
from selenium import webdriver


def main(driver):
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get("https://www.lagou.com/zhaopin/Java/?labelWords=label")
    driver.find_element_by_css_selector(".body-btn").click()
    while True:
        infoList = driver.find_elements_by_css_selector(".position_link h3")
        for info in infoList:
            info.click()
            driver.switch_to.window(driver.window_handles[1])
            company = driver.find_element_by_css_selector("h4.company")
            jobName = driver.find_element_by_css_selector("h1.name")
            salary = driver.find_element_by_css_selector("span.salary")
            experience = driver.find_element_by_css_selector(".job_request h3 span:nth-child(3)")
            print("公司: %s; 职位名称: %s; 薪资: %s; 工作经验: %s" % (company.text, jobName.text, salary.text, experience.text))
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(5)
        nextBtn = driver.find_element_by_css_selector(".pager_container a:last-child")
        if "pager_next_disabled" in nextBtn.get_attribute("class"):
            break
        nextBtn.click()


driver = webdriver.Chrome()
try:
    main(driver)
finally:
    driver.quit()
