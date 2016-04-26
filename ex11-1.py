print "What is your name?"
name = raw_input()
print "Sir %r HWHat is your quest?" %name
quest = raw_input()
print "What is the velocity of an unladen swallow?"
v = raw_input()
#the beginnings of input validation
if v[-1:] == '?':
	print "I don't know that!! --WHOOOSH--"
else:
	print "Go on then."
