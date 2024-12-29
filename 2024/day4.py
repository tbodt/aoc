import aoc
from collections import *
import re

inp='''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])
g = {}
for r, l in enumerate(inp.splitlines()):
    for c, x in enumerate(l):
        g[r,c] = x

def places(w,h):
    for r in range(h):
        for c in range(w-3):
            yield [(r,c+i) for i in range(0,4)]
    for c in range(w):
        for r in range(h-3):
            yield [(r+i,c) for i in range(0,4)]
    for r in range(h-3):
        for c in range(w-3):
            yield [(r+i,c+i) for i in range(0,4)]
    for r in range(3,h):
        for c in range(w-3):
            yield [(r-i,c+i) for i in range(0,4)]

def solve():
    w = max(r for r,c in g)+1
    h = max(c for r,c in g)+1
    print(w,h)
    pg = {}
    n=0
    for p in places(w,h):
        x = ''.join(g[r,c] for r,c in p)
        if not (x == 'XMAS' or x == 'SAMX'): continue
        for r,c in p: pg[r,c] = g[r,c]
        n+=1
    for r in range(h):
        for c in range(w):
            print(pg.get((r,c),'.'),end='')
        print()
    print(n)

    def is_xmas(r,c):
        if r-1<0 or r+1>=h: return False
        if c-1<0 or c+1>=w: return False
        if g[r,c] != 'A': return False
        if g[r-1,c-1]+g[r+1,c+1] not in ['MS','SM']: return False
        if g[r-1,c+1]+g[r+1,c-1] not in ['MS','SM']: return False
        return True

    n = 0
    for r in range(h):
        for c in range(w):
            n += is_xmas(r,c)
    print(n)

if __name__ == '__main__':
    solve()
