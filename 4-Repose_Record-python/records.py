#!/usr/bin/env python3

import sys
import copy
import re


pattern1 = re.compile('\[(....)\-(..)\-(..) (..):(..)\] (.*)')
pattern2 = re.compile('.* \#(\d*) .*')

class Guard:
    all = dict()

    def __init__(self, id_):
        self.asleep = 0
        self.minutes = dict()
        self.all[id_] = self

    def add_sleep(self, date, falls, wakes):
        self.asleep += wakes - falls
        for m in range(falls, wakes):
            if m not in self.minutes:
                self.minutes[m] = list()
            self.minutes[m].append(date)



def get_puzzle_input(file_input):
    data = ( x.strip() for x in open(file_input).readlines() )
    data = filter(None, data)
    data = list(data)
    tuple = data.sort()
    return data

def parse(data):
    id_ = None
    fell = None
    for line in data:
        action = None
        match = pattern1.match(line)
        ye, mo, da, h, m, rest = match.groups()
        if rest.startswith('Guard'):
            action = 'begins'
            id_ = int(pattern2.match(rest).groups()[0])
            if id_ not in Guard.all:
                Guard(id_)
        else:
            action = rest.split()[0]
            if action == 'falls':
                fell = m
            else:
                date = str(mo) + str(da)
                Guard.all[id_].add_sleep(date, int(fell), int(m))
        #print(ye, mo, da, h, m, id_, action)

def biggest_sleeper():
    d = Guard.all
    minutes = { d[k].asleep:k  for k in d.keys() }
    return minutes[max(minutes)]

def most_slept_minute(id_):
    minutes = Guard.all[id_].minutes
    freqs = { len(minutes[k]):k for k in minutes.keys() }
    frequence = max(freqs)
    minute = freqs[frequence]
    return frequence, minute


    


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('\nMissing data file.\n', file=sys.stderr)
        sys.exit(1)
    data = get_puzzle_input(sys.argv[1])
    parse(data)
    id_ = biggest_sleeper()
    print('ID of biggest sleeper: ', id_)
    print('minutes most slept: ', most_slept_minute(id_)[0])

