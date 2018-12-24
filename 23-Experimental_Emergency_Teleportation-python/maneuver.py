#!/usr/bin/env python3

import re
import sys

pattern = re.compile('pos=\<(.+),(.+),(.+)>.*r=(.+)')

max_dist = 0
max_idx = None
points = list()

def distance(p1, p2):
    return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1]) + abs(p2[2]-p1[2])

def read_data(fn):
    global max_dist
    global max_idx
    global points
    counter = 0
    with open(fn) as lines:
        for line in lines:
            nums = pattern.match(line.strip()).groups()
            if nums:
                nums = [ int(_) for _ in nums ]
                x, y, z, d = nums
                points.append((x, y, z))
                if d > max_dist:
                    max_dist = d
                    max_idx = counter
                counter += 1

def all_dist():
    in_range = 0
    for p in points:
        if distance(points[max_idx], p) <= max_dist:
            in_range += 1
    return in_range

read_data(sys.argv[1])
print('highest range: {} at point {}, coordinates {}'.format(max_dist, max_idx, points[max_idx]))
print(all_dist())
