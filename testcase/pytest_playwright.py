"""
#-*- coding:utf--8 -*-
#@Time    :2025/10/17 13:46
#@Author  :zjunbin
#@File    :pytest_playwright.py
"""
import re
from playwright.sync_api import Page, expect
"""
如果playwright 要允许pytest框架需要安装插件
pytest-playwright
默认是无头模式（正式运行选择无头模式，调试选有头模式）
"""

def test_example(page: Page) -> None:
    page.goto("https://www.baidu.com/")
    page.wait_for_timeout(2000)
    page.locator("//a[@id='s-top-loginbtn']").click()
    page.locator("//input[@name='userName']").fill('324')
    page.locator("//input[@id='TANGRAM__PSP_11__password']").fill('324')
    page.wait_for_timeout(5000)


    # page.get_by_role("link", name="登录").click()
    # page.get_by_role("textbox", name="手机号/用户名/邮箱").click()
    # page.get_by_role("textbox", name="手机号/用户名/邮箱").fill("32")
    # page.get_by_role("textbox", name="密码").click()
    # page.get_by_role("textbox", name="密码").fill("12")
    # page.get_by_role("checkbox", name="阅读并接受").check()
    # page.get_by_role("button", name="登录").click()
    # page.wait_for_timeout(3000)
    # expect(page.get_by_text("短信登录")).to_be_visible()
    # page.wait_for_timeout(3000)