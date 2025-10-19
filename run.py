"""
#-*- coding:utf--8 -*-
#@Time    :2025/10/17 14:19
#@Author  :zjunbin
#@File    :run.py
"""
'''自动发现、收集、运行生成测试allure报告'''
'查看测试报告   allure serve ./allure_report/'

import pytest

pytest.main(['-s', '-v', r'--alluredir=E:\djangoProject\playwright_test\allure_report', '--clean-alluredir'])
