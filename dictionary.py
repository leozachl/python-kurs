from pprint import pprint

teilnehmer = {
    'Eva': 1996,
    'Sascha': 1995,
    'Philip': 1994,
    'Reinhard': 1964,
    'Marcus': 1981,
    'Peter': 1980,
    'Leo': {'year': 1966, 'gender': 'm', 'edu': ['VS', 'Gym', 'HTL', 'TU'],},
    'Mark': 1975,
}

'''
pprint(teilnehmer)

names, years = zip(*teilnehmer)
print('Der jügnste Teilnehmer:', teilnehmer[years.index(max(years))])
print('Der älteste Teilnehmer:', teilnehmer[years.index(min(years))])


name = input("Name eines Teilnehmers ")

if name in teilnehmer:
    print (teilnehmer[name])
else:
    print ("gibts nicht")
'''
for name in teilnehmer:
    print(name, teilnehmer[name])

print (teilnehmer['Leo']['edu'][-1])