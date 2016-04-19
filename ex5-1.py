# -*- coding: utf-8 -*-

def in_cm(inches):
    return inches * 2.54
	
def lbs_kg(lbs):
	return lbs / 2.5
	
name = "Isaac Friedman"
age = 26 #Not a lie, but I'll have to start soon
height = 70 #inches
weight = 184 #lbs. also not a lie
eyes = 'Brown'
teeth = 'white'
hair = 'Brown'

print "Let's talk about %s." % name
#Confirming Unicode. The word is a Hebrew idiom for i.e.
print "He's %d inches tall, דהיינו %r centimeters." % (height, in_cm(height))
print "He's a bit overweight at %d but not too much." % weight
print "%r kg sounds better. Always use kg for your own weight and lbs for weight you can lift." % lbs_kg(weight)
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are %s depending on the coffee." % teeth

#80 column lines is a good habit to have
print "If I add %d, %d, and %d, I get %d, which is a meaningless number." % (
	age, height, weight, age + height + weight)