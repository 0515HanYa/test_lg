#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-10-30 23:38
# @Author : yooli
# @file : run.py
import unittest

if __name__ == '__main__':

	#方法四：匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
	#test_dir:被测试脚本的路径    pattern:脚本名称匹配规则
	test_dir = 'unitest'
	discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
	unittest.TextTestRunner(verbosity=2).run(discover)