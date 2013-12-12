provinces = {'Newfoundland': 'NF',
         'Quebec': 'QC',
         'Alberta': 'AL',
         'British Columbia': 'BC',
         'Ontario': 'ON'
        }

cities = {
        'BC': 'Vancouver',
        'AL': 'Calgary',
        'NF': 'St. Johns'
        }

cities['ON'] = 'Ottawa'
cities['QC'] = 'Montreal'

print ("-" * 100)
print ("ON State has: ", cities['ON'])
print ("QC State has: ", cities['QC'])

# print some provinces
print ('-' * 100)
print ("Ontario's abbreviation is: ", provinces['Ontario'])
print ("Quebec's abbreviation is: ", provinces['Quebec'])

# do it by using the province then cities dict
print ('-' * 100)
print ("Ontario has: ", cities[provinces['Ontario']])
print ("Quebec has: ", cities[provinces['Quebec']])

#print every province abbreviation
print ('-' * 100)
for province, abbrev in provinces.items():
    print ("{} is abbreviated {}".format(province, abbrev))

#print every city
print ('-' * 100)
for abbrev,city in cities.items():
    print ("{} has the city {}".format(abbrev, city))

#print both at the same time
print ('-' * 100)
for province, abbrev in provinces.items():
    print ("{} province is abbreviated {} and has city {}".format(province, abbrev, cities[abbrev]))

print ('-' * 100)
province = provinces.get('Nunavut', None)

if not province:
    print( "Sorry, no Nunavut")

#get a city with a default value
city = cities.get('NV', 'Does Not Exist')
print("The city for the province 'NV' is: {}".format(city))
