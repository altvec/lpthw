# Prompt user for a filename to open
filename = raw_input('Enter a filename to open: ')

# Open filename and assign file object to var txt
txt = open(filename)

# Printing filename
print "Here's your file %r:" % filename
# Printing txt object content
print txt.read()

# Close a file
txt.close()