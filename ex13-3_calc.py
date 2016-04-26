####
#More work with argv
#This time we will use argv to collect two operands and then use raw input to 
#ask for an arithmetic operation to perform on them. Effectively, we've just 
#made a basic calculator
####

from sys import argv

####
#See how we aren't checking to make sure the arguments are numbers? That is a 
#Very Bad Idea. Run the script with something other than numbers to find out 
#why.
####
script, first, second = argv #script is always an argument

#input is like raw_input except that it reads a python expression
op = raw_input("Which arithmetic operation would you like to perform?")
####
#Making sure your input is the right kind of data, and knowing what to do if it
#isn't is called "validation". This is a very simple kind of validation to make
#sure we were given an arithmetic operator.
####
if op in ['+','-','*','/','%','**']: #all the arithmetic python supports
	exp = first + op + second #makes an expression with our string in it
	result = eval(exp) #eval takes a string and treats it like python code
	print result
else:
	print "bad operation. goodbye" #this is a horrible way to handle errors
