from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_data = (open(from_file)).read()

out_file = open(to_file, 'w'); out_file.write(in_data)

out_file.close()

print "All done."
