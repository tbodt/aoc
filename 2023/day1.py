import aoc
from collections import *
import re

inp = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

numnames = ['one','two','three','four','five','six','seven','eight','nine']
numnames_ante = [a[::-1] for a in numnames]
digits = [str(a) for a in range(1,10)]

def alasa(line, numnames):
    firstp = float('inf')
    w = None
    for nasinnanpa in (numnames, digits):
        for i, d in enumerate(nasinnanpa):
            if d not in line: continue
            if line.index(d) < firstp:
                firstp = line.index(d)
                w = i+1
    return w

def firstdigit(line):
    return alasa(line, numnames)

def lastdigit(line):
    return alasa(line[::-1], numnames_ante)

def solve():
    # tot = 0
    # for a in inp.splitlines():
    #     d = [c for c in a if c.isdigit()]
    #     print(d)
    #     tot += int(d[0]+d[-1])
    # print(tot)
    tot = 0
    for a in inp.splitlines():
        tot += int(str(firstdigit(a)) + str(lastdigit(a)))
    print(tot)

if __name__ == '__main__':
    solve()
