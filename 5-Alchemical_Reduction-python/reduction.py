#!/usr/bin/env python3

import io
import sys


def get_puzzle_input(file_input):
    data = open(file_input).read().strip()
    return data


def one_pass(data):
    new_data = ''
    reductions = 0

    d = io.StringIO(data)
    first = d.read(1)
    while True:
        second = d.read(1)
        if second == '':
            new_data += first
            break
        if abs(ord(first) - ord(second)) == 32:
            reductions += 1
            first = d.read(1)
            if first  == '':
                break
        else:
            new_data += first
            first = second
    return reductions, new_data

def multi_passes(data):
    reductions = 1
    loops = 0
    while reductions > 0:
        loops += 1
        reductions, data = one_pass(data)
    return loops, data


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('\nMissing data file.\n', file=sys.stderr)
        sys.exit(1)
    data = get_puzzle_input(sys.argv[1])
    loops, new_data = multi_passes(data)
    print('length: {} in {} loops'.format(len(new_data), loops))

