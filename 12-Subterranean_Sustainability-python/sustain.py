#!/usr/bin/env python3

import sys
sys.setrecursionlimit(100000)

patterns = None

class pot:
    def __init__(self, state=False, idx=0, prev=None, nex=None):
        self.state = state
        self.prev = prev
        self.nex = nex
        self.idx = idx

    def get_quint(self):
        c = self.state
        a = b = d = e = False
        if self.prev:
            b = self.prev.state
            if self.prev.prev:
                a = self.prev.prev.state
        if self.nex:
            d = self.nex.state
            if self.nex.nex:
                e = self.nex.nex.state
        return (a, b, c, d, e)

    def get_left_most(self):
        # print(self.idx)
        if self.prev is None:
            return self
        else:
            return self.prev.get_left_most()

    def get_right_most(self):
        if self.nex is None:
            return self
        else:
            return self.nex.get_right_most()

    def insert(self, state=False):
        new = pot(state, idx=(self.idx - 1), nex=self)
        self.prev = new
        return new

    def append(self, state=False):
        new = pot(state, idx=(self.idx + 1), prev=self)
        self.nex = new
        return new

    def delete_collection(self):
        curr = self.get_right_most()
        while True:
            if curr.prev:
                p = curr
                curr = curr.prev
                del p
            else:
               break 

    def print_collection(self):
        curr = self.get_left_most()
        while True:
            #print(curr.idx)
            if curr.idx == 0:
                print('\033[1m', end='')
            if curr.state:
                print('#', end='')
            else:
                print('.', end='')
            if curr.idx == 0:
                print('\033[0m', end='')
            if curr.nex == None:
                print()
                break
            curr = curr.nex

def s_to_b(c):
    return True if c == '#' else False

def pad_pots(p):
    first = p.get_left_most()
    first = first.insert()
    first = first.insert()
    last = p.get_right_most()
    last = last.append()
    last.append()
    return first

def str_to_collection(s):
    s = s.strip()
    first = pot(state=s_to_b(s[0]), idx=0)
    prev = first
    for letter in s[1:]:
        state = s_to_b(letter)
        prev = prev.append(state)
        last = prev
    first = pad_pots(first)
    return first

def new_gen(prev_gen_first):
    old = prev_gen_first.get_left_most()
    curr = pot(state=prev_gen_first.state, idx=prev_gen_first.idx)
    old = old.nex
    while True:
        state = True if old.get_quint() in patterns else False
        curr = curr.append(state=state)
        if old.nex:
          old = old.nex
        else:
            break
    first = pad_pots(curr)
    return first

def sum_idx(f):
    total = 0
    curr = f.get_left_most()
    while True:
        if curr.state:
            total += curr.idx
        if curr.nex:
            curr = curr.nex
        else:
            break
    return total

def load_file(fn):
    first = None
    patterns = list()
    for line in open(fn):
        line = line.strip()
        if len(line) == 0:
            continue
        if line.startswith('initial state:'):
            _, init_state = line.split(':')
            first = str_to_collection(init_state)
        else:
            pattern, result = line.split('=>')
            pattern = pattern.strip()
            result = result.strip()
            if result == '#':
                pattern = tuple(map(s_to_b, pattern))
                patterns.append(pattern)
    return first, tuple(patterns)



if __name__ == "__main__":
    gen_0, patterns = load_file(sys.argv[1])
    gen_first = gen_0
    #gen_first.print_collection()
    for i in range(1, 21):
        gen_first = new_gen(gen_first)
    #gen_first.print_collection()
    print('Total sum of index with flowers after 20 generations: {}'.format(sum_idx(gen_first)))
    for i in range(1, 50000000001):
        gen_first = new_gen(gen_first)
    print('Total sum of index with flowers after 50000000000 generations: {}'.format(sum_idx(gen_first)))


