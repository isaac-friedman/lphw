#Warning: This joke requires having seen Monty Python and the Holy Grail, or at
#the very least having been on the internet long enough to get some of the
#jokes.
print "What is your name?"
name = raw_input()
print "Sir %r HWHat is your quest?" %name
quest = raw_input()
print "What is the velocity of an unladen swallow?"
v = raw_input()
#the beginnings of input validation
#This grabs the last character of the string and checks to see if you answered
#a question with a question. If you did, our bridge guardian dies of paradox
if v[-1:] == '?':
	print "I don't know that!! --WHOOOSH--"
else:
	print "Go on then."
