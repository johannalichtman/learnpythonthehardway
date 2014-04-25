from sys import argv

# argv is the 'argument variable' 
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "your third variable is:", third

first = raw_input("What is your age? ") #how do I turn variable name into a string?
second = raw_input("What is your height? ")
third = raw_input("What is your weight? ")

print "So you're %r old, %r tall and $%r heavy." % (
	first, second, third)
