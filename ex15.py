from sys import argv

# get file using argv

script, filename = argv	

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

# get file using raw_input

print "Type the filename again:" 
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# close files at end to free up memory

txt.close()
txt_again.close()