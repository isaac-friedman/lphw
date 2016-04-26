from sys import argv

script, user_name = argv
prompt = '> '

print "Hi, %s! I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" %user_name
likes = raw_input(prompt)

print "Where do you live, %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
You said %s about liking me. I like you anyway because i'm a friendly 
artificial unintelligence!
You said you live in %s. Don't know where that is.
You said you have a %s computer. Cool!
""" %(likes, lives, computer)
