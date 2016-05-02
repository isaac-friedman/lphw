####
#Introduction to functions and variables.
#It is good Python practice (people who like that sort of thing say 'Pythonic')
#to keep function definitions at the top of the file. Without going into all
#the arguments, this way makes sense when you think about it. After all, when
#you import libraries, the interpreter puts the code at the top of the file
####

####
#cheese_and_crackers looks at how much cheese and crackers you have and tells
#you to quit reading my workthrough of a very simple tutorial and spend some
#time with your friends.
####
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	
	####
	#The line below checks that you have at least 3 cheeses and at least
	#one box of crackers for each cheese. Imagine you were actually trying
	#to figure out if you have enough cheese and crackers for a party; how
	#would you make this function more useful?
	####
	if(cheese_count > 3 and boxes_of_crackers >= cheese_count):
		print "Man, that's enough for a party!"
	print "Get a blanket! \n"

print "We can pass numbers to the function directly:"
cheese_and_crackers(20,30)

print "Or, we can use variables from our script:"

#In "real" programming, this is the right way to do it most of the time because
#it makes it easy to keep the number of cheeses consistent throughout.
cheeses = 10
cracker_boxes = 50
cheese_and_crackers(cheeses, cracker_boxes)

print "You can also pass arithmetic expressions."
#IMPORTANT: Do not put quotes around expressions. If you do, they get read as
#strings and your function will not work
cheese_and_crackers(10+5, 5+6)

print "We're gonna do that again to test the conditional."
#Is this an expression, or a string?
cheese_and_crackers(1+1, 7)
cheese_and_crackers(5-1, 3)

print "Or both, while modifying a variable"
#Variable names can be part of expressions too even though they're all letters.
cheese_and_crackers(cheeses*5, cracker_boxes + 27)
