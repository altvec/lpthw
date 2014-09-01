from sys import argv

script, input_file = argv

# print all content of the file 'f'
def print_all(f):
    print f.read()

# Move to the beginning of the file 'f'
def rewind(f):
    f.seek(0)

# Print one line of the file 'f'
def print_a_line(line_count, f):
    print line_count, f.readline()

# Input file object
current_file = open(input_file)

print "First let's print the whole file:\n"

# Call function print_all
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# Call function rewind
rewind(current_file)

# Print first three lines of file
print "Let's print three lines:"

# We can replace current_line var from original exercise with
# this (iterates over range of integers from 1 up to, but not
# including 4, e.g from 1 to 3), so we print exactly 3 lines
for i in xrange(1, 4):
    print_a_line(i, current_file)
