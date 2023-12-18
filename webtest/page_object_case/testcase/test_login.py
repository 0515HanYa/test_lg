#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-18 19:04
# @Author : yooli
# @file : test_login.py
import time

from webtest.page_object_case.page.baidumain import BaiduMain


class TestLogin:

	def setup(self):
		self.main2 = BaiduMain()

	def test_login(self):
		assert self.main2.goto_login().goto_register()
		time.sleep(3)
		self.main2._driver.quit()