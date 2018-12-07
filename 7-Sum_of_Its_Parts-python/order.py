#!/usr/bin/env python3

import re
import argparse
import logging

logging.basicConfig(format='==> %(module)s, %(funcName)s %(message)s', level=logging.ERROR)

pattern = re.compile('Step (.) must be finished before step (.) can begin')

nexts = dict()
prevs = dict()
firsts = None

def get_puzzle_input(file_input):
    data = ( x.strip() for x in open(file_input) )
    data = [ (pattern.match(x).groups()) for x in data ]
    return data

def organise(data):
    global nexts
    global firsts

    for a, b in data:
        if a not in nexts:
            nexts[a] = list()
        nexts[a].append(b)
        if b not in prevs:
            prevs[b] = list()
        prevs[b].append(a)
    alphas, betas = [ x for x in zip(*data) ]
    firsts = set(alphas).difference(set(betas))
    logging.debug('firsts: {}:'.format(firsts))
    firsts = list(firsts)

def follow_tree(firsts):
    stack = list()

    firsts = list(firsts)
    firsts.sort()
    cur = firsts[0]
    if len(firsts) > 0:
        stack.extend(firsts[1:])

    result = [cur]

    while True:
        logging.debug('result: {}'.format(result))
        logging.debug('stack: {}'.format(stack))
        logging.debug('cur: {}'.format(cur))
        if cur in nexts:
            for e in nexts[cur]:
                if e not in stack and e not in result:
                    stack.append(e)
        stack.sort()
        newcur = ''
        for i, candidate in enumerate(stack):
            if candidate in firsts or set(prevs[candidate]).issubset(result):
                newcur = candidate
                del stack[i]
                break
        if newcur in result or newcur == '':
            break
        else:
            cur = newcur
            result += cur
    return result



        



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
    organise(data)
    print(''.join(follow_tree(firsts)))
    #for a,b in data:
    #    print('{} -> {};'.format(a, b))



