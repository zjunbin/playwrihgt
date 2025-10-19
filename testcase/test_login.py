"""
#-*- coding:utf--8 -*-
#@Time    :2025/10/17 14:11
#@Author  :zjunbin
#@File    :test_login.py
"""
import re
from playwright.sync_api import Page, expect
"""
如果playwright 要允许pytest框架需要安装插件
pytest-playwright
默认是无头模式（正式运行选择无头模式，调试选有头模式）
"""
from page_object.login_page import LoginPage
import pytest

data = [
    {"username": "12", "password": "231"},
    {"username": "33", "password": "23"},
    {"username": "21", "password": "12313"},
]

@pytest.mark.parametrize('data',data)
def test_login(page: Page,data) -> None:
    page.goto("https://www.baidu.com/")
    lg = LoginPage(page=page)
    lg.login_page(username=data['username'],password=data['password'])
    lg.assert_()

