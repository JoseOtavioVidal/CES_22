import sys

def is_factor(f,  n):
	"""Analyse if f is a factor of n"""
	if n%f == 0:
		return True
	else:
		return False


def test(is_ok):
	"""Print is the test is ok or not"""
	linenum = sys._getframe(1).f_lineno
	if is_ok:
		msg = "Test in line {0} is ok".format(linenum)
	else:
		msg = "Test in line {0} is not ok".format(linenum)
	print(msg)	
		
		
def suite_test():
	"""Make a set of test to make sure the fuction is_factor is ok"""
	test(is_factor(3,12))
	test(not is_factor(5,12))
	test(is_factor(7,14))
	test(not is_factor(7,15))
	test(is_factor(1,15))
	test(is_factor(15,15))
	test(not is_factor(25,15))
	
#Run the set of tests
suite_test()