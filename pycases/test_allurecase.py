#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-12-06 22:47
# @Author : yooli
# @file : test_allurecase.py

import pytest

def test_success():
	assert True

def test_failure():
	assert False

def test_skip():
	pytest.skip('for a reason!')

def test_breaken():
	raise Exception