import unittest

def add(a,b):
	return a + b
	
class Testcase01(unittest.Testcase):
	def testcase_01(self):
		print("testcase_01")
		print("1+1=",add(1,1))
		
	def testcase_02(self):
		print("testcase_02")