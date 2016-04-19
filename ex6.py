x = "There are %d kinds of people in the world." %10

binary = "binary"
do_not = "don't"

#How to hold places for multiple variables.
#You can do heterogenous types but it's a bad idea
y = "Those who know %s and those who %s." %(binary, do_not)

#variables. not complicated
print x
print y
'''
This part is fun. %r prints raw data, while %s prints a formatted string.
%r can be used for digits, binary, doubles, points etc, so when it's a string
the interpreter tells us by enclosing it in single quotes. %r is useful for 
debugging %s is for output to users
'''
print "I said: %r " %x
print "I also said: '%s' " %x

hilarious = False
joke_evaluation = "Isn't that joke funny? %r"
print joke_evaluation % hilarious

print "You have now learned more about string formatting and played with some complex strings."
print "Sorry for the horrible joke."

n = "This is the left half ... "
m = "of a string with a right side."

print n+m
