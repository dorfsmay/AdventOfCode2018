#!/usr/bin/env python3

import sys

def get_puzzle_input(file_input):
    data = open(file_input).readlines()
    data = ( x.strip() for x in data )
    data = [ int(x) for x in data if len(x) > 0 ]
    return tuple(data)

def calculate_resulting_freq(data):
    return sum(data)

def frist_duplicate_freq(data):
    results = set()
    runs = 0
    result = 0
    while True:
        runs += 1
        if runs%20 == 0:
            print(runs, "iterations")
        for e in data:
            result += e
            if result in results:
                print()
                return result, runs
            else:
                results.add(result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('\nMissing data file.\n', file=sys.stderr)
        sys.exit(1)
    data = get_puzzle_input(sys.argv[1])
    resultfreq = calculate_resulting_freq(data)
    first_dupe = frist_duplicate_freq(data)
    print("Resulting frequency:", resultfreq)
    print("First duplicate frequency: {} (in {} runs)\n".format(*first_dupe))

