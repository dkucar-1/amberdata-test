import os
from process_words import read_file, words_and_lengths, odd_words, sorted_words

path = os.path.join(os.getcwd(),'words.json')                    
data = read_file(path)
odd_w = [e[0] for e in odd_words(data)]
sorted_w = sorted_words(data)

def test_words_and_lengths():
    assert len(words_and_lengths(data)) > 0, 'There is no content in the words file'

def test_odd_words():
    assert len(odd_w) > 0, 'There are odd length words in the list'

def test_sorted_words():
    test_list = [len(v) for v in sorted_words(data)]
    assert all(a <= b for a, b in zip(test_list, test_list[1:])), 'The list isn\'t sorted properly.'
 