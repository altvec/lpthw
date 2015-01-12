def while_loop(max, incr):
    numbers = []
    i = 0
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + incr
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i

    print "The numbers:"
    for num in numbers:
        print num

while_loop(4, 1)
print "========"
while_loop(10, 2)
