print "Let's practice everything."
#This is not how to use escapes. Normally you choose double quotes if you know
#your string will have lots of 's, but we're proving a point here.
print 'You\'d have to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %d" %five

"""All functions should have docstrings
	

"""
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars /100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of %d" %start_point
print "We'd have %d beans, in %d jars, packed into %d, crates." %(beans, jars, crates)

start_point /= 10

print "We can also do that this way:"
print "We'd have %d beans, in %d jars, packed into %d, crates." %(beans, jars, crates)
