import aoc
from collections import *
import re

inp='''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def solve():
    tot=0
    for a in inp.splitlines():
        cardnum = int(a.split(': ')[0].split()[1])
        winners = [int(x) for x in a.split(': ')[1].split(' | ')[0].split()]
        drawn = [int(x) for x in a.split(': ')[1].split(' | ')[1].split()]
        #print(winners,drawn)
        s = (set(winners).intersection(set(drawn)))
        print(s)
        if len(s):
            tot += 2**(len(s)-1)
    print(tot)

    howmany = [1]*len(inp.splitlines())
    tot=0
    for i, a in enumerate(inp.splitlines()):
        cardnum = int(a.split(': ')[0].split()[1])
        winners = [int(x) for x in a.split(': ')[1].split(' | ')[0].split()]
        drawn = [int(x) for x in a.split(': ')[1].split(' | ')[1].split()]
        #print(winners,drawn)
        s = (set(winners).intersection(set(drawn)))
        for wi in range(i+1, i+1+len(s)):
            howmany[wi] += howmany[i]
    print(sum(howmany))

if __name__ == '__main__':
    solve()
