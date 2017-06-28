import random

zahl = random.randint(0,100)

i = 0
while i < 10:
    try:
        user_input = int(input("Zahlenraten:"))
        if zahl == user_input:
            print ("You got it!")
            break
        elif (user_input < zahl):
            print("zu klein")
        else:
            print("zu groß")
        i += 1

    except:
        print("eine Zahl!")
        continue

if zahl != user_input:
    print(zahl, "wäre es gewesen")