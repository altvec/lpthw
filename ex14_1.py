from sys import argv

script, user_name, age = argv
prompt = '% '
age = int(age)

print "Hi %s, I'm the %s script." % (user_name, script)
print "So, you're %d years old." % age
print "I'd like to ask you for a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You are %d years old.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, age, lives, computer)