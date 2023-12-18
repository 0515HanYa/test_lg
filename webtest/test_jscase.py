#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-15 15:49
# @Author : yooli
# @file : test_jscase.py
import time

import pytest

from webtest.base import Base
from selenium.webdriver.common.by import By

class TestJs(Base):

	@pytest.mark.skip
	def test_js_scroll(self):
		self.driver.get("https://www.baidu.com/")
		self.driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("selenium测试")
		# return：可以返回js的返回结果
		element = self.driver.execute_script("return document.getElementById('su')")
		element.click()
		time.sleep(3)
		self.driver.execute_script("document.documentElement.scrollTop=10000")
		self.driver.find_element(By.XPATH,"//*[@id='page']/div/a[10]").click()
		time.sleep(3)

		for code in [
			"return document.title","return JSON.stringify(performance.timing)"
		]:
			print(self.driver.execute_script(code))

		# print(self.driver.execute_script("return document.title"))
		# print(self.driver.execute_script("return JSON.stringify(performance.timing)"))

	def test_datatime(self):
		self.driver.get("https://www.12306.cn/index/")

		# self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
		# self.driver.execute_script("a.value='2023-12-31'")
		# time.sleep(3)
		for c in [
			"a=document.getElementById('train_date')",
			"a.removeAttribute('readonly')",
			"return a.value='2023-12-31'"
		]:
			print(self.driver.execute_script(c))
		time.sleep(3)