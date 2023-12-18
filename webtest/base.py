#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-14 0:58
# @Author : yooli
# @file : base.py

from selenium import  webdriver

class Base:
	def setup(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(3)

	def teardown(self):
		self.driver.quit()