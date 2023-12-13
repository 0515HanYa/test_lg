#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-13 10:04
# @Author : yooli
# @file : test_actions.py
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestActions:
	def setup(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(3)

	def teardown(self):
		self.driver.quit()

	@pytest.mark.skip
	def test_case_click(self):
		self.driver.get("https://sahitest.com/demo/clicks.htm")
		element_click = self.driver.find_element(By.XPATH,"//input[@value='click me']")
		element_right_click = self.driver.find_element(By.XPATH, "//input[@value='right click me']")
		element_dbl_click = self.driver.find_element(By.XPATH, "//input[@value='dbl click me']")

		action = ActionChains(self.driver)
		action.click(element_click)
		action.context_click(element_right_click)
		action.double_click(element_dbl_click)
		action.perform()
		time.sleep(3)

	@pytest.mark.skip
	def test_moveelem(self):
		self.driver.get("https://www.baidu.com/")
		element_move = self.driver.find_element(By.XPATH,"//*[@id='s-usersetting-top']")
		action2 = ActionChains(self.driver)
		action2.move_to_element(element_move)
		action2.perform()
		time.sleep(3)

	@pytest.mark.skip
	def test_dragelem(self):
		self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
		element_drag = self.driver.find_element(By.XPATH,"//*[@id='dragger']")
		element_drop = self.driver.find_element(By.XPATH,'/html/body/div[3]')
		ation3 = ActionChains(self.driver)
		#实现拖拽效果的三种方式
		ation3.drag_and_drop(element_drag,element_drop)

		# ation3.click_and_hold(element_drag)
		# ation3.release(element_drop)

		# ation3.click_and_hold(element_drag)
		# ation3.move_to_element(element_drop)
		# ation3.release(element_drop)

		ation3.perform()
		time.sleep(3)


	def test_keys(self):
		self.driver.get("https://sahitest.com/demo/label.htm")
		element_web = self.driver.find_element(By.XPATH,'/html/body/label[1]/input')
		action4 = ActionChains(self.driver)
		element_web.click()
		action4.send_keys("yooli").pause(1)
		action4.send_keys(Keys.SPACE).pause(1)
		action4.send_keys("Hanna").pause(1)
		action4.send_keys(Keys.BACKSPACE).pause(1)
		# action4.send_keys_to_element(element_web,"yooli")
		action4.perform()
		time.sleep(3)


if __name__ == '__main__' :
	pytest.main({'-v','-s','test_actions.py'})