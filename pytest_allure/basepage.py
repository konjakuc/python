# -*- coding: utf-8 -*-

import os
import time
from selenium.webdriver.common.by import By
from logger import getLogger

logger = getLogger("BasePage")
IMG_DIR = os.path.dirname(os.path.abspath(__file__)) + '/screenshots/'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://www.baidu.com"

    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    def open(self, url=None):
        self.driver.get(url if url else self.url)
        logger.info("Open page with url %s" % (url if url else self.url))

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except Exception as e:
            logger.error("Failes to quit the browser with %s" % e)

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "tag":
            return By.TAG_NAME
        else:
            logger.info("Locator type " + locator_type + " not correct/supported")
        return False

    def element_get(self, locator, locator_type="id", web_element=None):
        element = web_element
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            if element:
                element = web_element.find_element(by_type, locator)
                logger.info(
                    "Element descendant Found with locator: " + locator
                    +", locator_type " + locator_type
                )
            else:
                element = self.driver.find_element(by_type, locator)
                logger.info(
                    "Element Found with locator: " + locator
                    +", locator_type " + locator_type
                )
        except:
            logger.error("Element not found")
        return element

    def element_click(self, locator='', locator_type='id', web_element=None):
        try:
            if web_element:
                web_element.click()
                logger.info("Clicked on element")
            else:
                element = self.element_get(locator, locator_type)
                element.click()
                logger.info(
                    "Clicked on element with locator: " + locator
                    +", locator_type: " + locator_type
                )
        except:
            logger.info(
                "Cannot click on the element with locator: " + locator
                +", locator_type: " + locator_type
            )

    def element_send_keys(self, locator, data, locator_type='id', element=None):
        try:
            if element is not None:
                element.send_keys(data)
            else:
                element = self.element_get(locator, locator_type)
                element.send_keys(data)
            logger.info(
                "Send data on element with locator: " + locator
                +", locator_type: " + locator_type
            )
        except:
            logger.info(
                "Cannot send data on element with locator: " + locator
                +", locator_type: " + locator_type
            )

    def get_windows_img(self):
        imgName = IMG_DIR + time.strftime('%Y%m%d%H%M',
                                          time.localtime(time.time())) + ".png"
        try:
            self.driver.get_screenshot_as_file(imgName)
            logger.info("Had take screenshot and save to folder: /screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to take screenshot! %s" % e)
