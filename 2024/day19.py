import aoc
import functools
from collections import *
import re

inp='''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])
towels, designs = inp.split('\n\n')
towels = set(towels.split(', '))
designs = designs.splitlines()
maxtowel = max(len(a) for a in towels)

@functools.cache
def test(design):
    print(design)
    if design == '': return 1
    ways = 0
    for tlen in range(1, maxtowel+1):
        if tlen > len(design): continue
        t = design[:tlen]
        if t in towels:
            ways += test(design.removeprefix(t))
    return ways

def solve():
    acc = 0
    ways = 0
    for d in designs:
        p = test(d)
        print(d, p)
        acc += bool(p)
        ways += p
    print(acc, ways)

if __name__ == '__main__':
    solve()
