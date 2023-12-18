#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-16 9:58
# @Author : yooli
# @file : test_fileupload.py
import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from webtest.base import Base


class TestFile(Base):
	@pytest.mark.skip
	def test_fileupload(self):
		self.driver.get("https://image.baidu.com/")
		self.driver.find_element(By.XPATH,"//*[@id='sttb']/img[1]").click()
		self.driver.find_element(By.CSS_SELECTOR,"#stfile").send_keys(r"D:\python_pro\test_lg\_DSC0104.JPG")
		time.sleep(3)

	def test_alert(self):
		self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
		self.driver.switch_to.frame("iframeResult")
		element_drag = self.driver.find_element(By.CSS_SELECTOR,"#draggable")
		element_drop = self.driver.find_element(By.CSS_SELECTOR,"#droppable")
		action = ActionChains(self.driver)
		action.drag_and_drop(element_drag,element_drop)
		action.perform()
		time.sleep(3)

		alt = self.driver.switch_to.alert
		print(alt.text)
		alt.accept()

		self.driver.switch_to.default_content()
		self.driver.find_element(By.CSS_SELECTOR,"#submitBTN").click()
		time.sleep(3)