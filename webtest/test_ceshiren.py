#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-08 7:55
# @Author : yooli
# @file : test_ceshiren.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class TestCeshiren:
	def setup(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		#动态隐性等待：如果在时间内找到元素，进行下一步，否则等到相应的时间（全局的 每次操作前都进行）
		self.driver.implicitly_wait(5)

	def teardown(self):
		self.driver.quit()

	def test_ceshiren(self):
		self.driver.get("https://ceshiren.com/")
		self.driver.find_element(By.LINK_TEXT,"测试内推").click()
		# time.sleep(3)#强制等待页面加载完全
		self.driver.find_element(By.LINK_TEXT,"内推 + 职位发布，可使用微信添加安伶儿企业微信").click()
		# time.sleep(3)
		self.driver.find_element(By.LINK_TEXT,"linger7725").click()
		time.sleep(3)