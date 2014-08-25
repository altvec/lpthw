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

txt.close()