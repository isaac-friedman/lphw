#Google "nethack" for an idea of how intricate a game like this can get
prompt = '> '
print "You are facing three doors.  Do you go through door #1 or door #2?"
door = input(prompt)

print door
if door == 1:
	print "There's a giant bear here eating cheesecake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = input(prompt)
	if bear == 1:
		print "The bear  eats your face off and you die. Good job!"
	elif bear == 2:
		print "The bear eats your leg off and you die. Good job!"
	else:
		print "Doing %s is probably a better idea." %bear
elif door == 2:
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	insanity == input(prompt)
	if insanity == 1 or insanity == 2: print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The madness rots your eyeballs into a pool of muck. Good job!"
elif door == 3:
	print "You meet  an old man who smiles sardonically at you and says \"A rebel, I see.\""
	print '''Do you :
	1. Punch the old man.
	2. Whip out your sword.
	3. "Well the other two doors seemed like a hard sell..."
	'''
	sage = input(prompt)
	if sage == "nutritional anthropologist":
		print "Amir has materialized 4 feet above your head. Has fallen on you. You are not dead but 
else:
	print "You stumble around in a circle and fall on your knife and die. Good job."

