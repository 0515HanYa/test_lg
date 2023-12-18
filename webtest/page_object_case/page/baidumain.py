#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-17 1:08
# @Author : yooli
# @file : baidumain.py
from selenium.webdriver.common.by import By

from webtest.page_object_case.page.baidulogin import BaiduLogin
from webtest.page_object_case.page.baiduregister import BaiduRegister
from webtest.page_object_case.page.base_page import BasePage


class BaiduMain(BasePage):

	_base_url = "https://work.weixin.qq.com/"

	def goto_login(self):
		self.find(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
		return BaiduLogin(self._driver)

	def goto_register(self):
		self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
		return BaiduRegister(self._driver)
