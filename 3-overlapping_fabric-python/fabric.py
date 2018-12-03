#!/usr/bin/env python3

import sys
import copy
import re

canvas = dict()
nonoverlapping = set()

pattern = re.compile('\#(.*) \@ (.*),(.*): (.*)x(.*)')

def canvas_add_point(id_, h, v):
    if h not in canvas:
        canvas[h] = dict()
    if v not in canvas[h]:
        canvas[h][v] = set()
    canvas[h][v].add(id_)
    if len(canvas[h][v]) > 1:
        for p in canvas[h][v]:
            nonoverlapping.discard(p)

class Patch:
    def __init__(self, id_, hmargin, vmargin, length, height):
        self.id_ = id_
        self.hmargin = int(hmargin)
        self.vmargin = int(vmargin)
        self.length = int(length)
        self.height = int(height)
        nonoverlapping.add(self.id_)
        self.populate_canvas()

    def __repr__(self):
        return '#{} @ {},{}: {}x{}'.format(self.id_, self.hmargin, self.vmargin, self.length, self.height)

    def populate_canvas(self):
        for h in range(self.hmargin + 1,  self.hmargin + self.length + 1):
            for v in range(self.vmargin + 1,  self.vmargin + self.height + 1):
                canvas_add_point(self.id_, h, v)


def overlapping():
    total = 0
    for linenum in canvas:
        interm = ( len(x) for x in canvas[linenum].values() )
        interm = [ x for x in interm if x > 1 ]
        total += len(interm)
    return(total)


def get_puzzle_input(file_input):
    data = ( x.strip() for x in open(file_input).readlines() )
    data = filter(None, data)
    for e in data:
        match = pattern.match(e)
        if match:
            Patch(*match.groups())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('\nMissing data file.\n', file=sys.stderr)
        sys.exit(1)
    get_puzzle_input(sys.argv[1])
    print("Number of square where fabric overlap:", overlapping())
    print("id of non-overlapping(s) fabric:", nonoverlapping)

