def append_wrapper(n, step=1):
	'''Append every "stepth" integer up to n to a list and print the last element at the beginning and
	end of each iteration. Then print the list
	n -- the upper bound
	step -- the number to "count by" (default 1)
	'''
	numbers = range(0, n, step)
	print numbers

input_num = input("Count up to WHAT?!")
step = input("By HOW many?!")
if isinstance(input_num, int) and isinstance(step, int):
	append_wrapper(input_num, step)
else:
	print "Counting numbers only. This program will exit now."
