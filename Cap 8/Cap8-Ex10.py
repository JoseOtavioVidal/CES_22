import sys

def reverse(s):
	"""Returns a string who is a reverse of s"""
	r = ""
	for x in s:
		r = x+r
	return r
	
	
def is_palindrome(s):
	"""Analyse if s is a palindrome"""
	r = reverse(s)
	if r == s:
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
	"""Make a set of test to make sure the fuction is_palindrome is ok"""
	test(is_palindrome("abba"))
	test(not is_palindrome("abab"))
	test(is_palindrome("tenet"))
	test(not is_palindrome("banana"))
	test(is_palindrome("straw warts"))
	test(is_palindrome("a"))
	test(is_palindrome(""))
	
#Run the set of tests
suite_test()