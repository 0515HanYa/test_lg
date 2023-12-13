#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-09 13:03
# @Author : yooli
# @file : test_implicity.py

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestImplicity:
	def setup(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)

	def teardowm(self):
		self.driver.quit()

	def test_wait(self):
		self.driver.get("https://ceshiren.com/")
		self.driver.find_element(By.XPATH, '//*[@title="按类别分组的所有话题"]').click()
		self.driver.find_element(By.XPATH, "//*[@title='学习笔记']").click()
		# time.sleep(3) 便于观察
		# print("end")

		# def wait(x):
		# 	return len(self.driver.find_elements(By.XPATH,'//*[@class="nav-item_开源项目 开源项目 ember-view"]'))>=1
		# #显示等待 自己写函数
		# WebDriverWait(self.driver,10).until(wait)
		# self.driver.find_element(By.XPATH, '//*[@title="开源测试 开源项目"]').click()
		time.sleep(3)

		WebDriverWait(self.driver, 10).until(
			expected_conditions.element_to_be_clickable((By.XPATH, "//*[@class='link-top-line']")))
		self.driver.find_element(By.XPATH, "//*[@class='link-top-line']").click()
		time.sleep(4)

