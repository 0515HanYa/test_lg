#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-11-01 19:14
# @Author : yooli
# @file : test_parametrize.py
import pytest
import yaml


class TestPara:
	#参数化
	@pytest.mark.parametrize("a,b",[
		(10,20),
		(20,30),
		(3,9)
	])
	def test_p1(self,a,b):
		print( a + b )

	@pytest.mark.parametrize(("c","d"), [
		(10, 20),
		(20, 30),
		(3, 9)
	])
	def test_p2(self, c, d):
		print(c + d)

	#yaml数据参数化
	@pytest.mark.parametrize(["e","f"], yaml.safe_load(open('./data.yaml')))
	def test_p3(self, e, f):
		print(e + f)