from pprint import pprint

teilnehmer = [
    ['Eva', 1996, ],
    ['Sascha', 1995, ],
    ['Philip', 1994, ],
    ['Reinhard', 1964, ],
    ['Marcus', 1981, ],
    ['Peter', 1980, ],
    ['Leo', 1966, ],
    ['Mark', 1975, ],
]

pprint(teilnehmer)

names, years = zip(*teilnehmer)
print('Der jügnste Teilnehmer:', teilnehmer[years.index(max(years))])
print('Der älteste Teilnehmer:', teilnehmer[years.index(min(years))])


name = input("Name eines Teilnehmers ")

for participant in teilnehmer:
    if participant[0].lower() == name.lower():
        print(participant[0], 'geboren im Jahre', participant[1])
        break
else:
    print("nicht gefunden")
