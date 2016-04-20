print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)

#let's learn about bugs
print "So, you're %r old, %r tall, and %r heavy." % (weight, age, height)

print """
The above was a bug.
Can you see what it was?
Sure I can because I did it myself.
What kind of a bug is it?
Can you find it in the commit history? (This one is clearly labeled)
Bugs are important.
"""
