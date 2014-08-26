from sys import argv

script, filename = argv

print "Opening the file %s ...\n" % filename
file_hanler = open(filename)

print file_hanler.read()

file_hanler.close()