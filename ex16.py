####
#This script opens a file, deletes its contents, and asks for new contests to
#write to the file.
####
from sys import argv

script, filename = argv

#Instructions for the user. These are important
print "We are going to erase %r." % filename
print "If you do not want to do that hit, CTRL-C (^C."
print "If you do want to do that, hit ENTER/RETURN."

#Prompt the user
raw_input("?")

#Open the file for writing. By default, Python opens files as read-only to keep
#you from deleting them by accident. When you specify the "writing" option, it
#automatically 'truncates' the file (deletes the contents but keeps the file
#itself).
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#this line is not necessary
target.truncate()

print "Now I'm going to ask you for three lines."
#get lines
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."
#write them to the file. Note how `raw_input` doesn't capture the RETURN and
#you have to add a newline.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
