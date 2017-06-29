from plz import is_plz

def test():
    assert is_plz("A-4451") == True
    assert is_plz("D-44510") == False
    assert is_plz("A-0100") == False
    assert is_plz("a 9999") == True
    assert is_plz("a 1000") == True
    assert is_plz("a-111a") == False