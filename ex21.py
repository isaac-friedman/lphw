"""Takes two parameters a and b and returns their sum"""
def add(a, b):
	print "ADDING %d + %d" %(a,b)
	return a+b

"""Takes two parameters a and b and returns their a - b"""
def subtract(a, b):
	print "SUBTRACTING %d - %d" %(a,b)
	return a-b

"""Takes two parameters a and b and returns their a * b"""
def multiply(a, b):
	print "MULTIPLYING %d * %d" %(a,b)
	return a*b

"""Takes two parameters a and b and returns their a / b"""
def multiply(a, b):
def divide(a, b):
	print "DIVIDING %d / %d" %(a,b)
	return a/b

print "Now let's do some math with these functions."

age = add(30,5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(101,2)

print "\nAge: %d \nHeight: %d \nWeight: %d \nIQ: %d \n" %(age, height, weight, iq)

print "Here's a puzzle."

# weight + (height - (weight * (iq/2)))
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "This becomes ", what, ". Can you do that by hand?"
