from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") # this is the 'input' line -- user returns to continue or ^C to exit

print "Opening the file..."
target = open(filename, 'w') # 'w' parameter is for write

print "Truncating the file. Goodbye!"
target.truncate() # this is redundant because 'w' parameter truncates file automatically

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")


# exercise to replace 6 write commands with one (1) write command
line_combo = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(line_combo)
# print "%s\n%s\n%s\n" % (line1, line2, line3)

print "And finally, we close it."
target.close()