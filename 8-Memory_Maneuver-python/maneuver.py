#!/usr/bin/env python3

import sys
import argparse
import logging

logging.basicConfig(format='==> %(module)s, %(funcName)s %(message)s', level=logging.ERROR)

sys.setrecursionlimit(10000)


def get_puzzle_input(file_input):
    data = [ int(x.strip()) for x in open(file_input).read().strip().split() ]
    return data

class Node():
    all_ = list()

    def __init__(self, parent, n_child, n_meta):
        self.all_.append(self)
        self.parent = parent
        self.n_child = n_child
        self.n_meta = n_meta
        self.childs = list()
        self.metas = list()

def create_node(parent, data):
    n_child, n_meta = data[0:2]
    self = Node(parent, n_child, n_meta)
    data = data[2:]
    for i in range(n_child):
        node, data = create_node(self, data)
        self.childs.append(node)
    self.metas = data[0:n_meta]
    return self, data[n_meta:]

def sum_meta():
    total = 0
    for n in Node.all_:
        total += sum(n.metas)
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", "-d",
                         action='store_true',
                         help="Debug mode (very verbose)",
                        )
    parser.add_argument("args",
                        )

    args = parser.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    data = get_puzzle_input(args.args)
    create_node(None, data)
    print('Total metas: {}'.format(sum_meta()))

