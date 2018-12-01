#!/usr/bin/env python3

import sys

def get_puzzle_input(file_input):
    data = open(file_input).readlines()
    data = ( x.strip() for x in data )
    data = [ int(x) for x in data if len(x) > 0 ]
    return data

def calculate(data):
    return sum(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('\nMissing data file.\n', file=sys.stderr)
        sys.exit(1)
    data = get_puzzle_input(sys.argv[1])
    print(calculate(data))

