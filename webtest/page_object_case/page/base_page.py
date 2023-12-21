#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-17 8:25
# @Author : yooli
# @file : base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

class BasePage:
	_base_url = ""

	# 参数定义driver的作用：只在第一次时初始化driver时不传参数， 之后的调用都使用现有的driver作为参数传入，就不会再初始化
	def __init__(self, driver: WebDriver = None):
		self._driver = ""
		if driver is None:
			self._driver = webdriver.Chrome()
		else:
			self._driver = driver

		self._driver.maximize_window()
		self._driver.implicitly_wait(5)

		if self._base_url != "":
			self._driver.get(self._base_url)

	def find(self,by,locator):
		return self._driver.find_element(by,locator)