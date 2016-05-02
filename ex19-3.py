#5 different ways to call a function. 
#I'm not doing 10 to avoid being too repetitive
from sys import argv

####
#This function does nothing more than take a number and add 1 to it.
#You might be familiar with the ++ operator from other languages ranging from
#C to Javascript but, alas, python doesn't have it.
####
def plusplus(n):
	n = n+1
	#We're going to print the new n because you should get to see the
	#function do something. Normally, if you want your function to tell the
	#rest of the program what it did, you "return". The book will cover
	#that later.
	print n

#Method 1: get a command line argument and pass it to the function
print "You gave me an argument, I'll give you a bigger one!"
script, num = argv
plusplus(num)

#Method 2: call the function on the argument directly
print "Again!"
plusplus(argv[1]) #mind your parens and brackets

#Method 3: with a prompt
num = raw_input("I don't like that number. Gimme a different one.")
plusplus(num)

#Method 4: like Method 3, but showing you something very important about scope
n = raw_input("I don't like that number. Gimme a different one.") 
plusplus(n)

#Method 5: Modifying the parameter in the function call. What would happen if 
#you replaced the minus sign with an equals? Always ask the dangerous questions
plusplus(num - 3)

#Method 5.5, like method 5 but using the argv list directly. What is the real
#difference between the two? Which one is easier to read and work with?
plusplus(argv[1] - 3)
