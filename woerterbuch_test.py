from woerterbuch import translate

def test():
    assert translate('hund') == 'dog'
    assert translate('dog') == 'hund'
    assert translate('cat') == 'katze'
    assert translate('katze') == 'cat'
    assert translate('house') == 'haus'