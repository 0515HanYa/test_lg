#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-06 23:41
# @Author : yooli
# @file : test_feature_story.py
import pytest
import allure

@allure.feature("登录模块")
class TestLogin:
	@allure.story("登录成功")
	def test_login_success(self):
		print("这是登录：测试用例，登陆成功")
		pass

	@allure.story("登陆失败")
	def test_login_success_a(self):
		print("这是登录：测试用例，登陆失败")
		pass

	@allure.story("用户名缺失")
	def test_login_success_b(self):
		print("用户名缺失")
		pass

	@allure.story("密码缺失")
	def test_login_failure(self):
		with allure.step("点击用户名"):
			print("输入用户名")
		with allure.step("点击密码"):
			print("输入密码")
		print("点击登录")
		with allure.step("点击登录之后登陆失败"):
			assert '1' == 1
			print("登录失败")

	@allure.story("登录失败")
	def test_login_faiture_a(self):
		print("这是登录：测试用例，登录失败")
		pass

if __name__ == '__main__':
	pytest.main()
