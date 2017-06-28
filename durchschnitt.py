summe = 0
anzahl = 0
while summe <= 50:
    try:
        user_input = int(input("Bitte eine Zahl eingeben:"))
        anzahl += 1
        summe += user_input
    except:
        break


if anzahl > 0:
    print ("Summe: ", summe, "Anzahl: ", anzahl)
    print ("Durchschnitt = ", summe / anzahl)