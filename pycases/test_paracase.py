#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-01 16:36
# @Author : yooli
# @file : test_paracase.py
import pytest
import yaml


class TestDemo:
	@pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
	def test_demo(self,env):
		if 'test' in env :
			print("这是测试环境")
			print(env)
			print("测试环境的ip为:",env["test"])
			#如果传入的数据为字典格式，结果输出key
			#如果传入的数据为列表格式，结果输出
		if 'dev' in env :
			print("这是正式环境")
			print("正式环境的ip为：",env["dev"])

	def test_demo1(self):
		print(yaml.safe_load(open("./env.yaml")))
		#{'test': '127.0.0.1'}
