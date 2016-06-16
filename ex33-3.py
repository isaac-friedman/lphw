def append_wrapper(n, step=1):
	'''Append every "stepth" integer up to n to a list and print the last element at the beginning and
	end of each iteration. Then print the list
	n -- the upper bound
	step -- the number to "count by" (default 1)
	'''
	i=0
	numbers = []

	while i<n:
		#where we are at the beginning of the iteration
		print "At the top i is %d" % i

		numbers.append(i)

		#if we don't increment the loop will go on forever or until the OS stops it.
		i = i + step
		print "Numbers now: ", numbers
		#now look!
		print "At the bottom i is %d" % i

		print "The numbers: "

		for num in numbers:
			print num

input_num = input("Count up to WHAT?!")
step = input("By HOW many?!")
if isinstance(input_num, int) and isinstance(step, int):
	append_wrapper(input_num, step)
else:
	print "Counting numbers only. This program will exit now."
