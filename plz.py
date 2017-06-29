import re


def is_plz(plz):
    plz = re.sub(r'\s+', ' ', plz.strip())
    matches = re.search(r'^[Aa][- ]?[1-9]\d{3}$',plz)

    if matches:
        return True
    else:
        return False