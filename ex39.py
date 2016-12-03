states = {
    'Oregon': 'OR', 
    'Florida': 'FL', 
    'California': 'CA', 
    'Michigan': 'MI', 
    'New York': 'NY'
}


cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY']= 'New York'
cities['OR']= 'Portland'

print("-"*15)
print("NY state has",cities['NY']) #The comma in a string puts a space in.  + does not.
print("OR state has "+cities['OR'])

print("-"*15)
print("Michigan's abbreviation is", states["Michigan"])  #single or double quotes doesn't matter-- it's still a string.
print("Florida's abbreviation is "+states['Florida'])

print("-"*15)
print("Michigan has:", cities[states["Michigan"]])
print("Florida has:", cities[states["Florida"]])

print("-"*15)
print(states.items())
for state, abbrev in states.items():
  print("%s is abbreviated as %s" %(state, abbrev))
#What is states.items()?  it appears to be a list of the contents of the dict?  
#print(isinstance(states.items(), list)) #this returns False?  

print("-"*15)
for abbrev, city in cities.items():
  print("%s has the city %s" %(abbrev, city))

print("-"*15)
for state, abbrev in states.items():
  print("%s has the city %s" %(state, cities[abbrev]))

print("-"*15)
state = states.get("Texas")
print(state)
state = states.get("California")
print(state)
state = states.get("Texas")
if not state:
  print("Sorry, no Texas")

print("-"*15)
city = cities.get('TX', "Sorry, doesn't exist") #the extra param is what gets returned in the event that the first param is not found, defaults to None
print(city)
city = cities.get('TX')
print(city)

#good comment in study drills: you could call a dictionary a lookup table. 
