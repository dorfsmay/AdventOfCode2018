#!/usr/bin/env python3

import sys

def get_puzzle_input(file_input):
    data = ( x.strip() for x in open(file_input).readlines() )
    data = [ x for x in data if len(x) > 0 ]
    return tuple(data)

def count_letters(word):
    letters = dict()
    for char in word:
        thiscount = 1 + letters.get(char, 0)
        letters[char] = thiscount
    return letters

def count_dupes(word):
    doubles = triples = False
    freqs = set(count_letters(word).values())
    doubles = 2 in freqs
    triples = 3 in freqs
    return (doubles, triples)

def checksum(data):
    duplicates = [ count_dupes(x) for x in data ]
    duplicates = tuple(map(list, zip(*duplicates)))
    return sum(duplicates[0]) * sum(duplicates[1])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('\nMissing data file.\n', file=sys.stderr)
        sys.exit(1)
    data = get_puzzle_input(sys.argv[1])
    print(checksum(data))
