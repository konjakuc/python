# -*- coding: utf-8 -*-

from basepage import BasePage
from logger import getLogger

logger = getLogger("BaiduPage")


class BaiduPage(BasePage):
    _search_input = "kw"
    _search_button = "su"

    def enter_search(self, content):
        self.element_send_keys(self._search_input, content)

    def click_search_button(self):
        self.element_click(self._search_button)

    def get_title(self):
        self.get_title()

    def search(self, content):
        self.enter_search(content)
        self.click_search_button()

