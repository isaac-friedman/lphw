####
#This file combines what we've learned about functionwas with what we've
#learned about files to show you how they can work together. It also
#sneaks in some more info about files which you may or may not know depending
#on if you did the study drills.
####
from sys import argv

#In some of my versions of the study drills, I access the arguments I want
#directly using [brackets]. Is this a good idea? Does it make any difference at
#all? Think about it.
script, input_file = argv

#read and print the whole file in one shot
def print_all(f):
	print f.read()

#move the iterator to the beginning of the file specified.
#Is printing necessary? Why or why not?
def rewind(f):
	print f.seek(0)

#Prints line line_count of file f
def print_a_line(line_count, f):
	print line_count, f.readline()

#Get a file object
current_file = open(input_file)

print "First let's print the whole file:\n"


print_all(current_file)

print """
We printed using a iterator *aaahh!!! scary word*. That iterator is now at the
end of the file, so we have to rewind it like a tape.
"""

#What happens if you comment out this line?
rewind(current_file)

print "Let's print all the lines one by one."

current_line = 1
print_a_line(current_line, current_file)

#If you think this repetition is silly, you're rights. Soon we will learn about
#loops which exist to solve this problem.
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
