try:
  user_input = int(input("Bitte eine Zahl eingeben: "))
except:
  exit("eine Zahl du x#%&§@!")

if user_input > 10:
  print ("user_input > 10")
elif user_input == 10:
  print("user_input == 10")
else:
  print("user_input < 10")

print("fertig")