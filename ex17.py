####
#This script copies one file to another
####
from sys import argv
from os.path import exists #this will be necessary to tell if a file exists outsid our script


script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

####
#This one is complicated. We are opening the file, just like we did in exercise
#16 but not naming it. Instead, we're using the 'read' function of an object 
#with no name (appropriately called an 'anonymous' object.) Also, notice how I
#said "use the 'read' function of" and not "use read on". That's because the 
#read function belongs to the file object. More on that later.
####
in_data = (open(from_file)).read()

#`len` is a built in python function. You can use it on all sorts of things.
print "The input file is %d bytes long." % len(in_data)

#exists just checks if something exists. the script does not know whether it is a file, let alone what kind.
print "Does the output file exist yet? %r" %exists(to_file)
print "Ready. Hit RETURN to continue, CTRL-C to abort()."
raw_input(">")

out_file = open(to_file, 'w'); out_file.write(in_data)

out_file.close()

print "All done."
