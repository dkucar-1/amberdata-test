#!/usr/bin/env python3
def read_file(path: str) -> str:
    """Given a path, return a JSON string."""
    import json
    with open(path, 'r') as file:
        data = json.load(file)
    return data

def words_and_lengths(data: str) -> dict:
    """Given a JSON string, form a dictionary of each word and its length."""
    """Assume the rows have key 'words'."""
    
    try:
        nested_words = [d['words'].split(' ') for d in data]
        # flatten nested list of lists as we get above
        all_words = sum(nested_words, [])
        # word is key, length of word is value
        return {word: len(word) for word in all_words}
    except:
        raise KeyError('You must use the key \'words\' for each line')

def odd_words(data: str) -> list:
    """From a dictionary of words and lengths, keep only odd length strings.
    Return list of tuples of word and its length."""
    all_words_dict = words_and_lengths(data)
    return [(word, num_chars) for word, num_chars in all_words_dict.items() if num_chars % 2 != 0]

def sorted_words(data: str) -> list: 
    """Using only odd length strings, sort by length in ascending order. 
    Return list of tuples of word and its length"""
    odd_numbers = odd_words(data)
    sorted_words = sorted(odd_numbers, key=lambda tup: tup[1])
    return [e[0] for e in sorted_words]


# call above functions in a script
if __name__ =="__main__": 
    import sys, os

    path = os.path.join(os.getcwd(), 'words.json') if len(sys.argv) == 1 else sys.argv[1]

    data = read_file(path)
    w_and_l = words_and_lengths(data)
    odd_w = [e[0] for e in odd_words(data)]
    sorted_w = sorted_words(data)
    print('**** Output ****')
    print('\n2. Words and their lengths:')
    print(w_and_l)
    print('\n3. List words with odd number of characters:')
    print(odd_w)
    print('\n4. Sort odd words in acending order of lengths:')
    print(sorted_w)
