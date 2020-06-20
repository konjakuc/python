# -*- coding: utf-8 -*-

import time
import pytest
from appium import webdriver

from common.data import command_executor, desired_caps

@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Remote(command_executor, desired_caps)
    driver.implicitly_wait(5)
    yield driver
    time.sleep(5)
    driver.quit()