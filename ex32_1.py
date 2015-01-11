the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count {0}".format(number)

# same as above
for fruit in fruits:
    print "A fruit of type: {0}".format(fruit)

# also we can go through mixed lists too
for i in change:
    print "I got {0}".format(i)

# we can also build lists
elements = xrange(0, 6)

# now we can print then out too
for i in elements:
    print "Element was: {0}".format(i)

