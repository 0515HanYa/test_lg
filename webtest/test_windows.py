#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-14 0:22
# @Author : yooli
# @file : test_windows.py
import time

from webtest.base import Base

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWindows(Base):

	def test_windows(self):
		self.driver.get("https://www.baidu.com/")
		self.driver.find_element(By.XPATH,"//*[@id='s-top-loginbtn']").click()

		print(self.driver.current_window_handle)
		print(self.driver.window_handles)

		self.driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_11__regLink').click()

		print(self.driver.current_window_handle)
		windows = self.driver.window_handles
		print(windows)
		print(self.driver.current_window_handle)

		time.sleep(3)

		self.driver.switch_to.window(windows[-1])
		print(self.driver.current_window_handle)
		self.driver.find_element(By.CSS_SELECTOR,"#TANGRAM__PSP_4__userName").send_keys("username")
		self.driver.find_element(By.CSS_SELECTOR,"#TANGRAM__PSP_4__phone").send_keys("phone")
		self.driver.find_element(By.CSS_SELECTOR,"#TANGRAM__PSP_4__password").send_keys("password")
		self.driver.find_element(By.CSS_SELECTOR,"#TANGRAM__PSP_4__verifyCode").send_keys("verifyCode")
		time.sleep(3)

		self.driver.switch_to.window(windows[0])
		print(self.driver.current_window_handle)
		self.driver.find_element(By.CSS_SELECTOR,"#TANGRAM__PSP_11__userName").send_keys("yooli")
		self.driver.find_element(By.CSS_SELECTOR,"#TANGRAM__PSP_11__password").send_keys("password")
		time.sleep(3)