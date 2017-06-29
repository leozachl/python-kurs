from plz import is_plz

valid = [
    "A-4451",
    "a 9999",
    "a 1000",
    "  A    1170   ",
]

invalid = [
    "D-44510",
    "A-0100",
    "a-11a1",
]

def test():
    for plz in valid:
        assert (is_plz(plz) == True)
    for plz in invalid:
        assert is_plz(plz) == False