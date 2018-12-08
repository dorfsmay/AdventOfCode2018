#!/usr/bin/env python3

import collections
import argparse
import logging

logging.basicConfig(format='==> %(module)s, %(funcName)s %(message)s', level=logging.ERROR)

grid = dict()
# OrderedDict is useful for debugging, because debug happens in the
# natural order.
#grid = collections.OrderedDict()
maxx = maxy = minx = miny = None
length = height = None
maxpos = None
edge = None

def get_puzzle_input(file_input):
    global maxx
    global maxy
    global minx
    global miny
    global length
    global height
    global maxpos
    data = list()
    for line in open(file_input):
            x, y = [ int(z.strip()) for z in line.split(',') ]
            data.append((x, y))
    maxx, maxy = [ max(z) for z in zip(*data) ]
    minx, miny = [ min(z) for z in zip(*data) ]
    return data

class Points:
    all_ = dict()
    id_counter = 0

    @classmethod
    def increment_counter(cls):
        cls.id_counter += 1

    def __init__(self, x, y):
        self.all_[self.id_counter] = self
        self.id_ = self.id_counter # Do we need this?
        self.increment_counter()
        self.x = x
        self.y = y
        self.where = list()
        self.alone = list()

class Locations:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_point = False
        self.closest_points = list()
        self.closest_distance = 0

    def add_point(self):
        self.is_point = True

def initialize_grid():
    for x in range(minx-1, maxx+2):
        for y in range(miny-1, maxy+2):
            grid[(x,y)] = Locations(x, y)

def add_points(data):
    for p in data:
        this = Points(*p)
        grid[(this.x, this.y)].add_point()

def distance(a, b):
    return abs(b.x - a.x) + abs(b.y - a.y)

def print_grid():
    print()
    for y in range(miny-1, maxy+2):
        line = ''
        for x in range(minx-1, maxx+2):
                loc = grid[(x,y)]
                if (x,y) in edge:
                    line += '~'
                elif loc.is_point:
                    line += 'X'
                else:
                    how_many = len(loc.closest_points)
                    if how_many == 0:
                        line += 'o'
                    elif how_many == 1:
                        line += str(loc.closest_points[0])
                    else:
                        line += '.'
        print(line)
    print()

def calculate_edge():
    global edge

    # Remove points have shortest distance from the edges
    edge = [ (x, miny-1) for x in range(minx-1, maxx+2) ]
    edge.extend( [ (x, maxy+1) for x  in range(minx-1, maxx+2) ] )
    edge.extend( [ (minx-1, y) for y in range(miny-1, maxy+2) ] )
    edge.extend( [ (maxx+1, y) for y  in range(miny-1, maxy+2) ] )
    logging.debug('Edge: {}'.format([ z for z in edge]))


def most_single():
    singles = collections.defaultdict(lambda: 1)
    mypoints = list(Points.all_.keys())

    # Remove point that have are single on the edge
    for pos in edge:
        points = grid[pos].closest_points
        if len(points) == 1:
            p = points[0]
            if p in mypoints:
                mypoints.remove(p)

    for pos, loc in grid.items():
        if len(loc.closest_points) == 1:
            point = loc.closest_points[0]
            if point in mypoints:
                singles[point] += 1
    return max(singles.values())

def calculate_distances():
    for pos, loc in grid.items():
        if not loc.is_point:
            for p in Points.all_.values():
                d = distance(loc, p)
                logging.debug('location: {}, Pt id_: {}'.format(pos, p.id_))
                logging.debug('new: {}, curr: {}, pts: {}'.format(d, loc.closest_distance, loc.closest_points))
                if loc.closest_distance == 0:
                    loc.closest_distance = d
                    loc.closest_points.append(p.id_)
                    p.where.append(pos)
                    p.alone.append(pos)
                else:
                    if d < loc.closest_distance:
                        for pp in loc.closest_points:
                            logging.debug('Removing {} from pos {}, {}'.format(pp, pos, Points.all_[pp].where))
                            loc.closest_points.remove(pp)
                            Points.all_[pp].where.remove(pos)
                            if pos in Points.all_[pp].alone:
                                Points.all_[pp].alone.remove(pos)
                        loc.closest_distance = d
                        loc.closest_points = [p.id_]
                        p.where.append(pos)
                        if len(p.where) == 1:
                            p.alone.append(pos)
                    elif d == loc.closest_distance:
                        for pp in loc.closest_points:
                            logging.debug('removing alone {} from pos {}, {}'.format(pp, pos, Points.all_[pp].where))
                            if pos in Points.all_[pp].alone:
                                Points.all_[pp].alone.remove(pos)
                        p.where.append(pos)
                        loc.closest_points.append(p.id_)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", "-d",
                         action='store_true',
                         help="Debug mode (very verbose)",
                        )
    parser.add_argument("--grid", "-g",
                         action='store_true',
                         help="Debug mode (very verbose)",
                        )
    parser.add_argument("args",
                        )

    args = parser.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    data = get_puzzle_input(args.args)
    initialize_grid()
    add_points(data)
    calculate_distances()
    calculate_edge()
    #print_grid()
    singles = most_single()
    print('Largest finite area:', singles)


