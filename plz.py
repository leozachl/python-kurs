import re

def is_plz(plz):
    if re.match('/^[Aa][- ]?[1-9]\d{3}$/',plz):
        return True
    else:
        return False

def test():
    assert is_plz("A-4451") == True
    assert is_plz("D-44510") == False
    assert is_plz("A-0100") == False
    assert is_plz("a 9999") == True
    assert is_plz("a 1000") == True
    assert is_plz("a-111a") == False

#plz = input("Bitte eine PLZ:")
#if is_plz(plz):
#    print("Könnte eine PLZ sein")
#else:
#    print("Ist keine österreichische PLZ")