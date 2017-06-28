text = "Monty Python ist super"

print(text.count('y'))
print(text.lower().count('p'))

print(text.find('ist'))

print(text.replace('ist','war'))

#for char in text:
#    print(char)
print (text[0:12])

words = text.partition(' ')
print (words)

words = text.split(' ')
print(words)