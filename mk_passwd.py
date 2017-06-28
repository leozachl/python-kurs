import random
import pytest

def mk_passwd(satz, min_words = 8, add_random_numbers = True):

    words = satz.split()
    if len(words) < min_words:
        raise ValueError('Too few words')
    pwd = ''
    for word in words:
        pwd += word[0]
        if add_random_numbers:
            pwd += str(random.randint(0,9))

    if add_random_numbers:
        return pwd[:-1]
    else:
        return pwd

def test():
    assert mk_passwd("We have found out that you are using a non-english keyboard layout", min_words=11, add_random_numbers=False) == 'Whfotyauankl'
    with pytest.raises(ValueError):
        mk_passwd("We have found out that you are using a non-english keyboard layout", min_words=13, add_random_numbers=False)