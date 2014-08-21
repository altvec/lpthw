name = 'Sergey K'
age = 28
height = 178 # cm
weight = 68 # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

def cm_to_inch(x):
    return x * 0.393701

def kg_to_pound(x):
    return x * 2.20462

print "Let's talk about %s." % name
print "He's %d centimeters or %d inches tall." % (height, cm_to_inch(height))
print "He's %d kilograms or %d pounds heavy." % (weight, kg_to_pound(weight))
print "Actually that's not too heavy."
print "He's got %s eyes and %r hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight,
    age + height + weight)