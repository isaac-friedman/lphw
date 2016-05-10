people = 30
cars = 30
trucks = 15

#are there more cars than people?
if cars > people:
	print "We should take the cars."
#what do you do if there are fewer?
elif cars < people:
	print "We should not take the cars."
#What if there are no more nor less? What does that even mean?
else:
	print "We can't decide."


if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we should take the trucks."
#There are exactly as many trucks as cars
else:
	print "We still can't decide."

if people > trucks:
	print "OK, let's just take the trucks."
else:
	print "Fine, let's stay home then."


