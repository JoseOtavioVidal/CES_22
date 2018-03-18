import sys
	
def add_vector(u, v):
	"""add two vectors"""
	w = []
	for i in range(len(u)):
		w.append(u[i]+v[i])
	return w


def scalar_mul(scalar, u):
	"""Multiple a vector by a scalar"""
	w = []
	for i in range(len(u)):
		w.append(u[i]*scalar)
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
	"""Make a set of test to make sure the fuction scalar_mul is ok"""
	test(scalar_mul(5, [1,2]) == [5,10])
	test(scalar_mul(3, [1,0, -1]) == [3, 0, -3])
	test(scalar_mul(7, [3,0,5, 11, 2]) == [21, 0, 35, 77, 14])
	
#Run the set of tests
suite_test()