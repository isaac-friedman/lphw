####
#This script prints a specified file to the screen. More specifically, it
#prints to something called "standard output" which is almost always the screen
#but could be something else. For now, think of 'print' as 'printing to the 
#screen' and 'standard output' or 'stdio' etc as "the screen." It's easier and
#pretty much always true.
####

#get the argv to be able to access command line arguments
from sys import argv

#Unpack your variables. You will always have to unpack your script because 
#argv reads (and counts) the arguments to the `python` command not to your
#script.
script, filename = argv

#txt is a 'file object'. You should google those because they're very important
#for I/O, and a good way to begin understanding how to use objects in
#programming
txt = open(filename)

print "Here is your file %r:" %filename
#Here, we call the `read` function OF the txt object. This function reads the
#file.
print txt.read()

#We do the same thing again, this time asking for input with a prompt
print "Type another file, or the same one for all I care."
#This is a nested function. Instad of putting the input in a variable,
#you can call `open` on it directly. Remember to have the same number of open
#and closed parentheses
nxt_txt = open(raw_input('> '))

print nxt_txt.read()
