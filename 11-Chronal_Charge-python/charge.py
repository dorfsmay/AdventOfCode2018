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

def calc_3_3_square_max_power(grid):
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

def calc_power_n_square(grid, start_x, start_y, sq_size):
    max_x = start_x + sq_size
    max_y = start_y + sq_size
    if (max_x > 299) or (max_y > 299):
        return None
    x_range = range(start_x, max_x)
    y_range = range(start_y, max_y)
    positions = itertools.product(x_range, y_range)
    val = sum( ( grid[pos] for pos in positions ) )
    return val

def calc_abs_max_power(grid):
    max_power = None
    max_x = None
    max_y = None
    max_size = None
    for y in range(1, 299):
        for x in range(1, 299):
            size = 1
            prev_max = 0
            while True:
                val = calc_power_n_square(grid, x, y, size)
                if val is None:
                    break
                if (max_power is None) or (val > max_power):
                    max_power = val
                    max_x = x
                    max_y = y
                    max_size = size
                prev_max = val
                size += 1
    return max_x, max_y, max_size




if __name__ == "__main__":
    if len(sys.argv) == 2:
        ser_num = int(sys.argv[1])
        grid = dict()
        populate_grid(grid, ser_num)
        squares_k, squares_v = calc_3_3_square_max_power(grid)
        max_power = highest_3_3(squares_v)
        print("3x3 square with max power: {}".format(max_power))
        print("max power square and size: {}".format(calc_abs_max_power(grid)))


