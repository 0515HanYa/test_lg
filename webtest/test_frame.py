#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-14 9:38
# @Author : yooli
# @file : test_frame.py
import pytest
from selenium.webdriver.common.by import By
from webtest.base import Base

class TestFrame(Base):

	def test_frame(self):
		self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
		self.driver.switch_to.frame("iframeResult")
		print(self.driver.find_element(By.CSS_SELECTOR, "#draggable").text)
		self.driver.switch_to.parent_frame()
		print(self.driver.find_element(By.CSS_SELECTOR, "#submitBTN").text)
		self.driver.quit()



