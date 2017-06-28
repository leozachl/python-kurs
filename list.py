teilnehmer = [
    'Eva',
    'Sascha',
    'Philip',
    'Reinhard',
    'Marcus',
    'Peter',
    'Leo',
]

def cmp(x, y):
    return len(x) > len(y)

participants = list(teilnehmer)
participants.insert(1,'Mark')

participants_orig = list(participants)
participants.sort
participants.sort()

print(participants)
print(participants_orig)

del(participants[3])
participants.remove('Leo')

print(participants)
participants.reverse()

print(participants.index('Eva'))
print(participants.pop(0))