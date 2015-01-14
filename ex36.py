from sys import exit

print "Adventures of the Jedi"

def mountain():
    print "There is a lonely mountain right ahead"

def emptyness():
    print "There is nothing interesting here."

def space_ship():
    print "This is your space ship"

def dead(cause):
    print cause
    exit(0)

def start():
    print "You have found yourself in the hot desert on unknown planet."
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
        dead("Attempting to {0} you're stuck in the sand, and after a few \
hours of unsuccessful attempts to escape - died.".format(choice))

start()
