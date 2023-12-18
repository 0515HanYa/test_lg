#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-17 1:10
# @Author : yooli
# @file : baidulogin.py
from selenium.webdriver.common.by import By

from webtest.page_object_case.page.baiduregister import BaiduRegister
from webtest.page_object_case.page.base_page import BasePage


class BaiduLogin(BasePage):
	def scan(self):
		pass

	def goto_register(self):
		self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
		return BaiduRegister(self._driver)