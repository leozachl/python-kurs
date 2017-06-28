import count_words
from pprint import pprint

words = []
while True:
    word = input('Bitte gib mir nur ein Wort: ')
    if word == '' or word == 'ENDE':
        break
    words.append(word)

pprint(count_words.count_word(words))
