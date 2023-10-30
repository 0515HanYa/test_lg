#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-10-30 10:21
# @Author : yooli
# @file : test_unitcase.py
import unittest

class TestStringMethods(unittest.TestCase):

#setUpClass和tearDownClass在所有测试case执行之前准备一次环境，在所有case执行结束之后再清理环境
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

# setUp和tearDown在每个测试方法(用例)前都进行准备环境和清理环境的操作
    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test_abc(self):
        print("abc_123")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print("test_upper")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print("test_isupper")

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
        print("test_split")

if __name__ == '__main__':
    unittest.main()