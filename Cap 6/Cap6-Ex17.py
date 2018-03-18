import sys

def is_multiple(n,  f):
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
	test(is_multiple(12,3))
	test(is_multiple(12,4))
	test(not is_multiple(12,5))
	test(is_multiple(12,6))
	test(not is_multiple(12,7))
	
#Run the set of tests
suite_test()