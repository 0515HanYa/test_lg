#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-21 17:43
# @Author : yooli
# @file : test_webfuyong.py
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestFuyong:

	def setup(self):
		opt = Options()
		opt.debugger_address = "127.0.0.1:9222"
		self.driver = webdriver.Chrome(options=opt)
		self.driver.get("https://kaiwu.lagou.com/learn")
		self.driver.maximize_window()
		self.driver.implicitly_wait(3)

	def test_fuyong(self):
		self.driver.find_element(By.CSS_SELECTOR,".username ").click()
		time.sleep(3)
		self.driver.find_element(By.LINK_TEXT,"账号设置").click()