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

    def get_states(self):
        states = list()
        curr = self.get_left_most()
        while True:
            states.append(curr.state)
            if not curr.nex:
                break
            curr = curr.nex
        return tuple(states)


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

    def print_collection(self):
        curr = self.get_left_most()
        while True:
            #print(curr.idx)
            if curr.idx == 0:
                print('\033[7m', end='')
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
    # We only need two extra empty pot on each end
    # Find left-most True value (plant)
    first = p.get_left_most()
    curr = first
    while curr.state is False:
        curr = curr.nex
    # move back 2 step
    if curr.prev:
        curr = curr.prev
        if curr.prev:
            curr = curr.prev
        else:
            # insert new one if there's only one
            curr = curr.insert()
    else:
        # insert 2 empty pots
        curr = curr.insert()
        curr = curr.insert()
    # severe link to potential previous pots
    curr.prev = None
    first = curr

    last = p.get_right_most()
    curr = last
    while curr.state is False:
        curr = curr.prev
    if curr.nex:
        curr = curr.nex
        if curr.nex:
            curr = curr.nex
        else:
            curr = curr.append()
    else:
        curr = curr.append()
        curr = curr.append()
    curr.nex = None
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

def stabilise(f):
    '''Does result set eventually stabilise (glides)?
    '''
    gen1 = f
    counter = 0
    while True:
        state1 = gen1.get_states()
        gen2 = new_gen(gen1)
        state2 = gen2.get_states()
        gen2.print_collection()
        if state2 == state1:
            return gen1, counter
        counter += 1
        gen1 = gen2



if __name__ == "__main__":
    gen_0, patterns = load_file(sys.argv[1])
    gen_first = gen_0
    gen_first.print_collection()
    for i in range(1, 21):
        gen_first = new_gen(gen_first)
        gen_first.print_collection()
    #gen_first.print_collection()
    print('Total sum of index with flowers after 20 generations: {}'.format(sum_idx(gen_first)))
    gen_first, generations = stabilise(gen_0)
    print('Stabilised on {} generation.'.format(generations))
    print('Total sum of index at generation {}: {}'.format(generations, sum_idx(gen_first)))
    print('Range from {} to {}.'.format(gen_first.get_left_most().idx, gen_first.get_right_most().idx))

