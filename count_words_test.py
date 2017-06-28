import pytest
import count_words

def test():
    test_patterns = [
                        [['foo'] * 5 + ['bar'] * 4 + ['foobar'] *3, {'foo': 5, 'bar': 4, 'foobar': 3}],
                        [['a'] * 100 + ['b'] * 99 + ['c'] * 49, {'a': 100, 'b': 99, 'c': 49}],
                        [[''], {'': 1}],
                        [['a'] * 5 + ['A'] *4, {'a': 5, 'A': 4}]
                    ]

    for test_pattern in test_patterns:
        assert count_words.count_word(test_pattern[0]) == test_pattern[1]
