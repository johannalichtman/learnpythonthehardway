print "How old are you?",	# comma at end so print doesn't end the line with newline
age = raw_input()			# raw_input stores data as a string
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
# height will output as 5\'5" because otherwise ' would end the string