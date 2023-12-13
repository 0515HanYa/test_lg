#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-12 19:40
# @Author : yooli
# @file : test_webcss.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestWeb:

	def setup(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(3)

	def teardown(self):
		self.driver.quit()

	def test_css(self):
		self.driver.get("https://ceshiren.com/")
		self.driver.find_element(By.CSS_SELECTOR,"#search-button").click()
		time.sleep(3)
		self.driver.find_element(By.CSS_SELECTOR,"#search-term").send_keys("定位")
		time.sleep(3)
		self.driver.find_element(By.CSS_SELECTOR,"#search-term").send_keys(Keys.ENTER)
		time.sleep(3)
		self.driver.find_element(By.CSS_SELECTOR, "#search-term").send_keys(Keys.ENTER)
		time.sleep(3)