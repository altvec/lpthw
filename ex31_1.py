print "You enter a dark room with two doors. Do you go through door #1 or door #2?"
door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Punch bear into his nose."
    bear = raw_input("> ")
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear >= "2" <= "3":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retuna."
    print "1. Blueberries."
    print "2. Yellow jacket clotherspins."
    print "3. Understanding revolvers yelling melodies."
    insanity = raw_input("> ")
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    elif insanity == "3":
        print "Listening those melodies cause your brain to explode. What do you do?"
        print "1. You are trying to collect the remains of your brain."
        print "2. You can see the music and trying to crawl to the nearby mushroom."
        explode = raw_input("> ")
        if explode == "1":
            print "There are too many picies, you found a couple and die. Good job!"
        elif explode == "2":
            print "You eat that mushroom and die. Good job!"
        else:
            print "You smell that mushroom and after 10 mins you get better. You win!"

    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
else:
    print "You stumble around and fall on a knife and die. Good job!"

