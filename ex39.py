#A mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

#A basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
}

#Some more cities
cities['NY'] = "New York"
cities['OR'] = "Portland"

#Print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#Print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#Print by using the states then cities dictionaries
print '-' * 10 
print "Michigan has: ", cities[states['Michigan']]
print "Florida's has: ", cities[states['Florida']]

#Print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

#Print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s state is abbreviated %s" % (abbrev, city)

#Now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
#Safely get an abbreviation of state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

#Get a city with a default value
city = cities.get('TX', 'Does not Exist')
print "The city for the state 'TX' is: %s" % city