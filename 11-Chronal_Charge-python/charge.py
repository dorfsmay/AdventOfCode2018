#!/usr/bin/env python3

import sys
import itertools

def calc_power(pos, ser_num):
    x, y = pos
    rackid = x + 10
    power = rackid * y
    power += ser_num
    power *= rackid
    power = str(power)
    try:
        power = int(power[-3])
    except IndexError:
        power = 0
    power -= 5
    return power

def populate_grid(grid, ser_num):
    for x in range(1, 301):
        for y in range(1, 301):
            grid[(x,y)] = calc_power((x,y), ser_num)

def calc_square_power(grid):
    squares_k = dict()
    squares_v = dict()
    for y in range(1, 299):
        for x in range(1,299):
            val = sum( (grid[pos] for pos in itertools.product((x, x+1, x+2), (y, y+1, y+2))) )
            squares_k[(x,y)] = val
            squares_v[val] = (x,y)
    return squares_k, squares_v

def highest_3_3(squares_v):
    max_power = max(squares_v.keys())
    return squares_v[max_power]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        ser_num = int(sys.argv[1])
        grid = dict()
        populate_grid(grid, ser_num)
        squares_k, squares_v = calc_square_power(grid)
        print("3x3 square with max power: {}".format(highest_3_3(squares_v)))

