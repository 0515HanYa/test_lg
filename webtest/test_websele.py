#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-07 18:57
# @Author : yooli
# @file : test_websele.py

from selenium import webdriver

def test_selenium():
	driver = webdriver.Chrome()
	driver.get("https://www.baidu.com/")