import configparser
from pprint import pprint

import os

def translate(word):
    config = configparser.ConfigParser()
    config.read(os.path.dirname(os.path.realpath(__file__)) + '/woerterbuch.ini')
    config.sections()
    en2de = config['words']
    zipped = zip(en2de.values(),en2de)
    de2en = dict(zip(en2de.values(),en2de))

    if word in en2de:
        return en2de[word.lower()]
    elif word in de2en:
        return de2en[word.lower()]
    else:
        return "i don't know"