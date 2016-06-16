i=0
numbers = []

while i<6:
	#where we are at the beginning of the iteration
	print "At the top i is %d" % i

	numbers.append(i)

	#if we don't increment the loop will go on forever or until the OS stops it.
	i = i + 1
	print "Numbers now: ", numbers
	#now look!
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num
