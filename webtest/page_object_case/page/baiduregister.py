#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-18 10:01
# @Author : yooli
# @file : baiduregister.py
from selenium.webdriver.common.by import By

from webtest.page_object_case.page.base_page import BasePage


class BaiduRegister(BasePage):

	def register(self):
		self.find(By.CSS_SELECTOR,"#corp_name").send_keys("yoolo")
		self.find(By.CSS_SELECTOR,"#manager_name").send_keys("yooli")
		self.find(By.CSS_SELECTOR,"#register_tel").send_keys("11111111111")
		self.find(By.CSS_SELECTOR, "#vcode").send_keys("1111")
		self.find(By.CSS_SELECTOR,"#iagree").click()
		self.find(By.CSS_SELECTOR,"#submit_btn").click()
		return True
