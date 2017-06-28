text = "Monty Python ist super"

print (text + text)
print(text.upper(), text.lower())
print(len(text))

if 'ist' in text:
    print("ist ist enthalten")

# user_input = input("text eingeben")

# if user_input.lower() in text.lower():
#    print (user_input, "in", text, "enthalten")

t = "Ein String 'ohne' \"Anführungszeichen\""
print(t)

a = 13
b = 7
print (a, "geteilt durch", b, "ergibt", a/b)

print ("%(a)d %(a)d geteilt durch %(b)02d ergibt %(ab)020.16f" % {'a': a,'b': b, 'ab': a/b})

print ("{0:d} geteilt durch {1:02d} ergibt {2:020.16f}".format(a, b, a/b))

print("{}")
