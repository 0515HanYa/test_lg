#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-10-31 12:43
# @Author : yooli
# @file : test_pytest.py
import pytest


def inc(x):
	return x+1

#参数化，生成多条测试用例
@pytest.mark.parametrize('a,b',[
	(1,2),
	(10,20),
	('a','a1'),
	(3,4),
	(5,6)
])

# def test_answer():
def test_answer(a,b):
	assert inc(a) == b
	# assert inc(4)==5

def test_answer1():
	assert inc(3) == 5

# a,c需要登录，b不需要登录
#pytest fixture装饰器
@pytest.fixture()
def login():
	print("登录操作")
	username = 'yooli'
	return username

class TestDemo:
	#执行test_a前先执行login,还可获取login返回的结果
	def test_a(self,login):
		print(f"a username = {login}")

	def test_b(self):
		print("b")

	def test_c(self,login):
		print(f"c  username = {login}")

if __name__ == '__main__':
	# pytest.main(['test_pytest.py'])
	pytest.main(['test_pytest.py::TestDemo','-v'])