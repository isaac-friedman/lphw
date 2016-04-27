from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file %r:" %filename
print txt.read()

print "Type another file, or the same one for all I care."
nxt_txt = open(raw_input('> '))

print nxt_txt.read()
