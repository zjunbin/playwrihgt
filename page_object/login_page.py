"""
#-*- coding:utf--8 -*-
#@Time    :2025/10/17 14:02
#@Author  :zjunbin
#@File    :login_page.py
"""
from playwright.sync_api import expect
import pytest
from common.basepage import BasePage

log_button = "//a[@id='s-top-loginbtn']"
phone = 'get_by_role("textbox", name="手机号/用户名/邮箱")'
pwd = 'get_by_role("textbox", name="密码")'
bt = 'get_by_role("checkbox", name="阅读并接受")'
dx  = 'get_by_text("短信登录")'

class LoginPage(BasePage):

    def login_page(self, username, password):
        self.click_ele(locator=log_button)
        # self.fill_value(locator=phone, value=username)
        # self.fill_value(locator=pwd, value=password)
        # self.click_ele(locator=bt)
        # self.page.wait_for_timeout(2000)
        # self.page.get_by_role("link", name="登录").click()
        # self.page.get_by_role("textbox", name="手机号/用户名/邮箱").click()
        # self.page.get_by_role("textbox", name="手机号/用户名/邮箱").fill(username)
        # self.page.get_by_role("textbox", name="密码").click()
        # self.page.get_by_role("textbox", name="密码").fill(password)
        # self.page.get_by_role("checkbox", name="阅读并接受").check()
        # self.page.wait_for_timeout(2000)
        # self.page.get_by_role("button", name="登录").click()
        # self.page.wait_for_timeout(2000)

    def assert_(self):
        # expect(self.page.get_by_text("短信登录")).to_be_visible()
        expect(self.click_ele(locator=dx)).to_be_visible()
