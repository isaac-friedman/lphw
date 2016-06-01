the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'bananas']
change = [1, 'pennies', 2, 'dimes', 3, 'quearters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

#same as above
for fruit in fruits:
	print "A fuit of type: %s" % fruit

#See how we can go through mixed lists too
#This is where %r is useful because we don't know what type we're printing
for i in change:
	print "I got %r" % i

#We can also built lists with loops. First start with an empty one
elements = []

#then use the range function to count from zero to 5. 
#Reread that last bit. It's important!
for i in range(0, 6): #range goes up to BUT DOESN'T INCLUDE the last element
	print "adding %d to the lists." % i
	#append is a function that lists understand. It does the same
	#thing as the English word 'append'
	elements.append(i)

# now we can print out our new list
for i in elements:
	print "Element was: %d" % i


