from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	print f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print """
We printed using a pointer *aaahh!!! scary word*. That pointer is now at the
end of the file, so we have to rewind it like a tape.
"""

rewind(current_file)

print "Let's print all the lines one by one."

current_line = 1
print_a_line(current_line, current_file)

#If you think this repetition is silly, you're rights. Soon we will learn about
#loops which exist to solve this problem.
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
