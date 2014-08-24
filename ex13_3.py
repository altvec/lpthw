from sys import argv

script, first, second = argv
third = int(raw_input("Enter third variable as number: "))

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is: %s %r" % (third, type(third))