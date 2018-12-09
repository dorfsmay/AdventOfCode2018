#!/usr/bin/env python3

import itertools
import collections
import argparse
import logging

logging.basicConfig(format='==> %(module)s, %(funcName)s %(message)s', level=logging.ERROR)

def high_score(num_players, last_marble):
    circle = [0, 1]
    players = collections.defaultdict(lambda: 0)
    idx = marble = 1

    for p in itertools.cycle(range(1, num_players+1)):
        logging.debug('[{}] {}'.format(p, circle))
        marble += 1

        if marble % 23 == 0:
           players[p] += marble
           idx = (idx - 7) % len(circle)
           removed = circle.pop(idx)
           logging.debug('Removing marble # {}'.format(removed))
           players[p] += removed
        else:
            len_c = len(circle)
            idx = (idx + 2) % len_c
            if idx == 0:
                circle.append(marble)
                idx = len_c
            else:
                circle.insert(idx, marble)
        if marble == last_marble + 1:
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

