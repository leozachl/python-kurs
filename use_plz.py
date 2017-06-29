from plz import is_plz


plz = input("Bitte eine PLZ:")
if is_plz(plz):
    print("Könnte eine PLZ sein")
else:
    print("Ist keine österreichische PLZ")