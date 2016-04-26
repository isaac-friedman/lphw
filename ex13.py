####
#Importing modules can serve 3 purposes if done right
#1-Allows you to add features to bare bones python
#2-Only importing what you need lets your imports serve as documentation for
#  someone else reading your code later.
#3-By forcing you to import things, python helps you keep your programs small
####

#import the 'hook' which lets python read command line arguments
from sys import argv

#argv is a list. This line puts all the elements into variables
script, first, second, third, fourth = argv

#You understand printing by now
print "Your script is called ", script, ", which was the zeroth variable."
print "Your first variable was ", first
print "Your second variable was ", second
print "Your third variable was ", third
print "Your first variable was ", first
