#!/usr/bin/env python3

import io
import sys
import re
import copy


def get_puzzle_input(file_input):
    data = open(file_input).read().strip()
    return data


def one_pass(data):
    d = list(data)

    
    first = 0
    second = 1
    while True:
        ##print(first, second)
        if second >= len(d):
            break
        if abs(ord(d[first]) - ord(d[second])) == 32:
            ####print(d)
            del d[first : second+1]
            if first == len(d):
                break
            first = 0 if first == 0 else first - 1
            second = first + 1
            ####print('reducing', len(d), first, second, d)
        else:
            first += 1
            second += 1
            l = len(d)
            if first >= l or second >= l:
                break
            ####print('moving', len(d), first, second)
    return ''.join(d)

multi_passes = one_pass

def shortest(data):
    lengths = list()
    for char in set(data.lower()):
        short_data = re.sub(char, '', data, flags=re.IGNORECASE)
        lengths.append(len(multi_passes(short_data)))
    return min(lengths)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('\nMissing data file.\n', file=sys.stderr)
        sys.exit(1)
    data = get_puzzle_input(sys.argv[1])
    new_data = multi_passes(data)
    print('length: {}'.format(len(new_data)))
    print('shortest:', shortest(data))

