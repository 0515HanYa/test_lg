#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-13 17:25
# @Author : yooli
# @file : test_touchAction.py
import time

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By

class TestTouchAction:

	def setup(self):

		opt = webdriver.ChromeOptions()
		opt.add_experimental_option('w3c', False)
		self.driver = webdriver.Chrome(chrome_options=opt)
		self.driver.maximize_window()
		self.driver.implicitly_wait(3)

	def teardown(self):
		self.driver.quit()

	def test_taction(self):
		self.driver.get("https://www.baidu.com/")
		el = self.driver.find_element(By.CSS_SELECTOR,'#kw')
		el_search = self.driver.find_element(By.CSS_SELECTOR,'#su')

		el.send_keys("selenium测试")
		action = TouchActions(self.driver)
		action.tap(el_search)
		action.perform()
		#拉到最底端
		action.scroll_from_element(el,0,2000).perform()
		time.sleep(3)


