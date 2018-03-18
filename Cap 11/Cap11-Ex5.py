import sys
	
def add_vector(u, v):
	"""add two vectors"""
	w = []
	for i in range(len(u)):
		w.append(u[i]+v[i])
	return w


def test(is_ok):
	"""Print is the test is ok or not"""
	linenum = sys._getframe(1).f_lineno
	if is_ok:
		msg = "Test in line {0} is ok".format(linenum)
	else:
		msg = "Test in line {0} is not ok".format(linenum)
	print(msg)	
		
		
def suite_test():
	"""Make a set of test to make sure the fuction add_vector is ok"""
	test(add_vector([1,1], [1,1]) == [2,2])
	test(add_vector([1,2], [1,4]) == [2,6])
	test(add_vector([1,2,1], [1,4,3]) == [2,6,4])
	
#Run the set of tests
suite_test()