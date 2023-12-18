#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-13 23:55
# @Author : yooli
# @file : test_form.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestForm:

	def setup(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(3)

	def teardown(self):
		self.driver.quit()

	def test_form(self):
		self.driver.get("https://www.baidu.com/")
		self.driver.find_element(By.XPATH,"//*[@id='s-top-loginbtn']").click()
		self.driver.find_element(By.XPATH,"//*[@id='TANGRAM__PSP_11__userName']").send_keys("username")
		self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__password"]').send_keys("password")
		self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__isAgree"]').click()
		self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__submit"]').click()
		time.sleep(3)