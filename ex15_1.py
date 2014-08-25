# Importing argv from sys module
from sys import argv

# Unpacking argv into script and filename vars
script, filename = argv

# Open filename and assign file object to var txt
txt = open(filename)

# Printing filename
print "Here's your file %r:" % filename
# Printing txt object content
print txt.read()

# Printing
print "Type the filename againg:"
# Prompting for a new filename (file_again)
file_again = raw_input("> ")

# Open file_again and assign file object to var txt_again
txt_again = open(file_again)

# Printing txt_again content
print txt_again.read()

# Closing both files
txt.close()
txt_again.close()