"""
#-*- coding:utf--8 -*-
#@Time    :2025/10/17 14:55
#@Author  :zjunbin
#@File    :basepage.py
"""
import re
from playwright.sync_api import Page, expect
class BasePage:
    def __init__(self,page: Page):
        self.page = page

    def locator(self,locator):
        element = self.page.locator(selector=locator)
        return element

    def click_ele(self,locator):
        self.locator(locator).click()

    def fill_value(self,locator,value):
        ele = self.locator(locator=locator)
        ele.fill(value=value)