from sys import argv

filename=argv[1]
print "Reading file %r" %filename
file = open(filename)
text = file.read()

print text
