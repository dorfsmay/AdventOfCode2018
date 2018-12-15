#!/usr/bin/env python3

import itertools
import collections
import argparse
import logging

logging.basicConfig(format='==> %(module)s, %(funcName)s %(message)s', level=logging.ERROR)

class Marbles:
    length = 0
    zero = None

    @classmethod
    def get_zero(cls):
        cls.zero = Marbles(0)
        cls.zero.prev = cls.zero.aft = cls.zero
        return cls.zero

    @classmethod
    def decrease(cls):
        cls.length -= 1

    @classmethod
    def increase(cls):
        cls.length += 1

    @classmethod
    def str(cls):
        values = list()
        this = cls.zero
        while True:
            values.append(str(this.value))
            this = this.aft
            if this == cls.zero:
                break
        return ', '.join(values)

    def __init__(self, value, prev=None, aft=None):
        self.prev = prev
        self.aft = aft
        self.value = value
        self.increase()

    def __repr__(self):
        return str(self.value)

    def remove(self):
        self.prev.aft = self.aft
        self.aft.prev = self.prev
        self.decrease()

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
        # Testing log level to prevent Marbles.str to be executed at
        # log level higher than DEBUG
        if logging.getLogger().level == logging.DEBUG:
            logging.debug('[%s] %s', p, Marbles.str())
        new_marble += 1

        if new_marble % 23 == 0:
           players[p] += new_marble
           remove = cur.walk(-7)
           cur = remove.aft
           logging.debug('Removing marble # %s. New cur: %s', remove, cur)
           players[p] += remove.value
           remove.remove()
        else:
            cur = cur.walk(2)
            cur = cur.insert(new_marble)
        if new_marble == last_marble + 1:
            break
    logging.debug(players)
    return max(players.values())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", "-d",
                         action='store_true',
                         help="Debug mode (very verbose)",
                        )
    parser.add_argument("players",
                        type=int,
                        )
    parser.add_argument("last_marble",
                        type=int,
                        )

    args = parser.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    hs = high_score(args.players, args.last_marble)
    print('High Score:', hs)
    

