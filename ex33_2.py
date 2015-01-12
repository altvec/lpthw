def for_loop(max, incr):
    numbers = []
    for i in range(0, max, incr):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now:", numbers
        print "At the bottom i in %d" % i

    print "The numbers:"
    for num in numbers:
        print num


for_loop(5, 1)
print "======"
for_loop(9, 2)
