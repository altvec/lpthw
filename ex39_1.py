# create a mapping of state to abbreviation
regions = {
    'Bashkortostan': 'BASH',
    'Tatarstan': 'TAT',
    'Moscow': 'MO',
    'Saint Petersburg': 'SPB'
}

# create a basic set of states and some cities in them
cities = {
    'BASH': 'Ufa',
    'TAT': 'Kazan',
    'MO': 'Dolgoprudny',
    'SPB': 'Saint-Petersburg'
}

# add some more cities
cities['BASH'] = 'Salavat'
cities['MO'] = 'Zelenograd'

# print out some cities
print '-' * 10
print "MO region has:", cities['MO']
print "SPB region has:", cities['BASH']

# print some states
print '-' * 10
print "Moscow's abbreviation is:", regions['Moscow']
print "Bashkortostan's abbreviation is:", regions['Bashkortostan']

# do it by using the state then cities dict
print '-' * 10
print "Moscow has:", cities[regions['Moscow']]
print "Bashkortostan has:", cities[regions['Bashkortostan']]

# print every state abbreviation
print '-' * 10
for region, abbrev in regions.items():
    print "%s is abbreviated %s" % (region, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for region, abbrev in regions.items():
    print "%s region is abbreviated %s and has city %s" % (region, abbrev,
                                                           cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
region = regions.get('Perm')
if not region:
    print "Sorry, no Perm."

# get a city with a default value
city = cities.get('PERM', 'Does Not Exist')
print "The city for the state 'PERM' is: %s" % city
