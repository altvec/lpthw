# Put a sting in a var x
x = "There are %d types of people." % 10
# Put a string in a var 'binary'
binary = "binary"
# Put a string in a var 'do_not'
do_not = "don't"
# Put a string in a var 'y'
y = "Those who know %s and those who %s." % (binary, do_not)

# print content from the var 'x'
print x
# print content from the var 'y'
print y

# print a formatted strings
print "I said: %r." % x
print "I also said: '%s'." % y

# set var 'hilarious' to True
hilarious = True
# put a string to a var 'joke_evaluation'
joke_evaluation = "Isn't that joke so funny?! %r"

# print a formatted string from var 'joke_evaluation'
print joke_evaluation % hilarious

# put a string to a var 'w'
w = "This is the left side of..."
# put a string to a var 'e'
e = "a string with a right side."

# print concatenated strings from variables 'w' and e'
print w + e