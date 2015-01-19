from sys import exit

print "Adventures of the Jedi"

WITH_MASTER = False


def mountain():
    global WITH_MASTER
    print "\nThere is a lonely mountain right ahead of you."
    print "You can see a strange spiral sign on the rock."
    print "1. Touch the sign"
    print "2. Yell at sign"
    print "3. Go back"
    choice = raw_input("> ")
    if choice == "touch" and WITH_MASTER is False:
        print "Nothing happened."
        mountain()
    elif choice == "touch" and WITH_MASTER is True:
        print "Mount opens and you see grand master Yoda."
        dead("Congratulations, you win!")
    elif choice == "yell":
        dead("A giant rock fall of the cliff and smashed you.")
    elif choice == "back":
        start()
    else:
        print "Probably doing {} is not great idea.".format(choice)
        mountain()


def emptyness():
    dead("Giant desert worm eats you.")


def space_ship():
    global WITH_MASTER
    print "\nThis is your space ship and you master is awaiting you."
    print "1. Ask a master to go with you."
    print "2. Kick master's butt."
    print "3. Go back"
    choice = raw_input("> ")
    if choice == "ask":
        print "Master go with you."
        WITH_MASTER = True
        space_ship()
    elif choice == "kick":
        dead("Master cuts your head off.")
    elif choice == "back":
        start()
    else:
        dead("You stumble around and fell on your lightsaber.")


def dead(cause):
    print cause
    exit(0)


def start():
    print "\nYou have found yourself in the hot desert on unknown planet."
    print "You look around and see lonely mountain on North,"
    print "barely visible space ship on East,"
    print "clouds of dust on South and West."
    print "What would you like to do?"
    choice = raw_input("> ")
    if "North" in choice:
        mountain()
    elif "South" in choice or "West" in choice:
        emptyness()
    elif "East" in choice:
        space_ship()
    else:
        dead("Attempting to {} you're stuck in the sand, \
and after a few hours of unsuccessful \
attempts to escape - died.".format(choice))

start()
