import aoc
from collections import *
import re
import math

inp='''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def solve():
    dirs = inp.splitlines()[0]
    g = {}
    nodes = inp.splitlines()[2:]
    for n in nodes:
        start, left, right = re.findall(r'[0-9A-Z]{3}', n)
        g[start] = left, right

    #n = 'AAA'
    #c = 0
    #i = 0
    #while n != 'ZZZ':
    #    #print(n, c)
    #    d = dirs[c % len(dirs)]
    #    l, r = g[n]
    #    if d == 'L': n = l
    #    elif d == 'R': n = r
    #    else: raise
    #    c += 1
    #print(c)

    n = [x for x in g if x.endswith('A')]
    cc = []
    for i in range(len(n)):
        c=0
        while True:
            #print(i, n,c)
            d = dirs[c % len(dirs)]
            n1 = n[i]
            l, r = g[n1]
            if d == 'L': n1 = l
            elif d == 'R': n1 = r
            else: raise
            n[i] = n1
            c += 1

            if n1.endswith('Z'): break
        cc.append(c)
    print(cc)
    print(math.lcm(*cc))


if __name__ == '__main__':
    solve()
