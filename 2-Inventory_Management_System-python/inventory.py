#!/usr/bin/env python3

import sys
import copy

def get_puzzle_input(file_input):
    data = ( x.strip() for x in open(file_input).readlines() )
    data = filter(None, data)
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

def matching_ids(alpha, beta):
    zipped = ( (pos, tup) for pos,tup in enumerate(zip(alpha, beta)) )
    positions = [ x[0] for x in zipped if x[1][0] != x[1][1] ]
    if len(positions) == 1:
        p = positions[0]
        return (alpha[:p] + alpha[p+1:])
    else:
        return None

def find_boxes(data):
    boxes = set()
    workset = list(set(data))
    while workset:
        first = workset.pop(0)
        box = ( matching_ids(first, x) for x in workset )
        # we use a set of the initial data, so we know we can have only one match
        box = tuple(filter(None, box))
        if box:
            boxes.add(box[0])
    return boxes

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('\nMissing data file.\n', file=sys.stderr)
        sys.exit(1)
    data = get_puzzle_input(sys.argv[1])
    print('Checksum:', checksum(data))
    print('Common letters:', find_boxes(data))

