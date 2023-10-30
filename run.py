#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-10-30 23:38
# @Author : yooli
# @file : run.py
import unittest

from HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':

	report_title = 'SY测试用例执行报告'
	desc = '用于展示修改样式后的HTMLTestRunner'
	report_file = 'TestReport.html'

	#方法四：匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
	#test_dir:被测试脚本的路径    pattern:脚本名称匹配规则
	test_dir = 'unitest'
	discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
	# unittest.TextTestRunner(verbosity=2).run(discover)

	with open(report_file, 'wb') as report:
		runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
		runner.run(discover)