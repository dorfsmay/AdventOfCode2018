#!/usr/bin/env python3

import re
import sys
import time

pattern = re.compile('position=< *(-?\d*), *(-?\d*)> velocity=< *(-?\d*), *(-?\d*)>')


positions = list()
velocities = list()
for line in open(sys.argv[1]):
    m = pattern.match(line)
    if m:
        x, y, vx, vy = m.groups()
        x, y, vx, vy = int(x), int(y), int(vx), int(vy)
        positions.append((x, y))
        velocities.append((vx, vy))

allx, ally = zip(*positions)
minx = min(allx) ; maxx = max(allx)
miny = min(ally) ; maxy = max(ally)
#print(minx, maxx, miny, maxy)
length = len(positions)

def move():
    global positions
    newpos = list()
    for i in range(length):
        newpos.append((positions[i][0] + velocities[i][0],
                       positions[i][1] + velocities[i][1],
                      )
                     )
    positions = newpos

def print_it():
    for y in range(miny, maxy+1):
        line = ''
        for x in range(minx, maxx+1):
            if (x,y) in positions:
                line += ('#')
            else:
                line += ('.')
        print(line)

while True:
    print()
    print_it()
    time.sleep(2)
    move()
    print()

