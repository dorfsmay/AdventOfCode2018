#!/usr/bin/env python3

import itertools
import collections
import argparse


class Marbles:
    zero = None

    @classmethod
    def get_zero(cls):
        cls.zero = Marbles(0)
        cls.zero.prev = cls.zero.aft = cls.zero
        return cls.zero

    def __init__(self, value, prev=None, aft=None):
        self.prev = prev
        self.aft = aft
        self.value = value

    def remove(self):
        self.prev.aft = self.aft
        self.aft.prev = self.prev

    def insert(self, value):
        new = Marbles(value, self.prev, self)
        self.prev.aft = new
        self.prev = new
        return new

    def append(self, value):
        new = self.zero.prev.insert(value)
        return new

    def walk(self, steps):
        this = self
        for s in range(0, abs(steps)):
            if steps > 0:
                this = this.aft
            if steps < 0:
                this = this.prev
        return this

def high_score(num_players, last_marble):
    zero = Marbles.get_zero()
    cur = zero.append(1)
    players = collections.defaultdict(lambda: 0)
    new_marble = 1

    for p in itertools.cycle(range(1, num_players+1)):
        new_marble += 1

        if new_marble % 23 == 0:
           players[p] += new_marble
           remove = cur.walk(-7)
           cur = remove.aft
           players[p] += remove.value
           remove.remove()
        else:
            cur = cur.walk(2)
            cur = cur.insert(new_marble)
        if new_marble == last_marble + 1:
            break
    return max(players.values())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("players",
                        type=int,
                        )
    parser.add_argument("last_marble",
                        type=int,
                        )

    args = parser.parse_args()
    hs = high_score(args.players, args.last_marble)
    print('High Score:', hs)
    

