from sys import argv

script, user_name, location = argv
prompt = '$ '

print "Hi, %s! I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" %user_name
likes = raw_input(prompt)

print "Where do you live, %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

if location != lives:
	print "You are not at home"

print """
You said %s about liking me. I like you anyway because i'm a friendly 
artificial unintelligence!
You live in %s. Don't know where that is.
You said you have a %s computer. Cool!
""" %(likes, lives, computer)
