#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-18 15:01
# @Author : yooli
# @file : test_register.py
import time
from webtest.page_object_case.page.baidumain import BaiduMain

class TestRegister:

	def setup(self):
		self.main = BaiduMain()

	def test_register(self):
		# assert False == self.main.goto_register().register()
		assert self.main.goto_register().register()
		time.sleep(3)
		self.main._driver.quit()