def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	if(cheese_count > 3 and boxes_of_crackers >= cheese_count):
		print "Man, that's enough for a party!"
	print "Get a blanket! \n"

print "We can pass numbers to the function directly:"
cheese_and_crackers(20,30)

print "Or, we can use variables from our script:"
cheeses = 10
cracker_boxes = 50

cheese_and_crackers(cheeses, cracker_boxes)

print "You can also pass arithmetic expressions."
cheese_and_crackers(10+5, 5+6)

print "We're gonna do that again to test the conditional."
cheese_and_crackers(1+1, 7)
cheese_and_crackers(5-1, 3)

print "Or both, while modifying a variable"
cheese_and_crackers(cheeses*5, cracker_boxes + 27)
