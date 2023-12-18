#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-14 13:22
# @Author : yooli
# @file : bases.py
import os
from selenium import  webdriver
class Base:
	def setup(self):
		browser = os.getenv("browser")
		if browser == "firefox":
			print("ff")
			self.driver = webdriver.Firefox()
		elif browser == "headless":
			self.driver = webdriver.phantomjs()
		else:
			self.driver = webdriver.Chrome()

		self.driver.maximize_window()
		self.driver.implicitly_wait(3)

	def teardown(self):
		self.driver.quit()