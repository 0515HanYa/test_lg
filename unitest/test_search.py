#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-10-30 13:28
# @Author : yooli
# @file : test_search.py
import unittest

class Search():

	def search(self):
		print("searching...")
		return True

class TestSearch1(unittest.TestCase):

	def setUp(self) -> None:
		print("setUp方法级别")
		self.search = Search()

	def tearDown(self) -> None:
		print("tearDown方法级别")

#每个用例前都要进行初始的实例化操作，因此可setUpClass设置
	def test_searching1(self):
		print("searching1")
		# search = Search()
		assert True == self.search.search()

	def test_searching2(self):
		print("searching2")
		# search = Search()
		assert True == self.search.search()

	def test_searching3(self):
		print("searching3")
		# search = Search()
		assert True == self.search.search()

class TestSearch(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		print("setUpClass类级别")
		cls.search = Search()

	@classmethod
	def tearDownClass(cls) -> None:
		print("tearDownClass类级别")

#每个用例前都要进行初始的实例化操作，因此可setUpClass设置
	def test_searching1(self):
		print("searching1")
		# search = Search()
		assert True == self.search.search()

	def test_searching2(self):
		print("searching2")
		# search = Search()
		assert True == self.search.search()

	def test_searching3(self):
		print("searching3")
		# search = Search()
		assert True == self.search.search()

	def test_equal(self):
		print("断言相等")
		self.assertEqual(1,1,"判断 1 == 1")
		self.assertEqual(1,2,"判断 1 == 2")

	def test_notEqual(self):
		print("断言不相等")
		self.assertNotEqual(1,2, "判断 1 ！= 1")
		# self.assertNotEqual(1,1,"判断 1 ！= 1")
		# self.assertTrue(1==2,"verify")

if __name__ == '__main__':

	#方法一：执行当前文件所有的测试用例
    # unittest.main()

	#方法二：执行指定的测试用例,将要执行的测试用例添加到套件里，批量执行
	#创建一个测试套件testsuite
	# suite = unittest.TestSuite()
	# suite.addTest(TestSearch1('test_searching1'))
	# suite.addTest(TestSearch('test_equal'))
	# runner = unittest.TextTestRunner()
	# runner.run(suite)

	#方法三：执行指定的测试类
	suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
	suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
	suite3 = unittest.TestSuite([suite1,suite2])
	unittest.TextTestRunner(verbosity=2).run(suite3)