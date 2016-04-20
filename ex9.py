days = "Monday Tuesday Wednesday Thursday Friday"
#behold the newline!
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
#remember the newline I told you about? This is where it happens
print "Here are the months: ", months

#printing the days and months as a formatted string gets you the same result
print "Here are the days: %s" %days
#remember the newline I told you about? This is where it happens
print "Here are the months: %s" %months

#but look what happens when you use raw data.
#This is why raw data is for debugging
print "Here are the days: %r" %days
#remember the newline I told you about? This is where it happens
print "Here are the months: %r" %months

print '''
This is strange
You can type
as many lines as 
you 
want without a newline character.
PS you can use these for comments too but you shouldn't.
'''
