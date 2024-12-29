import aoc
import copy
from collections import *
import re

inp='''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

DIRS = [(-1,0),(0,-1),(1,0),(0,1)]

def rotate_cw(g, h, w):
    g2 = {}
    for r in range(h):
        for c in range(w):
            g2[c,h-1-r] = g[r,c]
    return g2

def tilt(g, h, w):
    for r in range(h):
        for c in range(w):
            if g[r,c] == 'O':
                # puush
                tr = r - 1
                while tr >= 0 and g[tr,c] == '.':
                    tr -= 1
                tr += 1
                g[r,c] = '.'
                g[tr,c] = 'O'

def cycle(g, h, w):
    tilt(g, h, w)
    g = rotate_cw(g,h,w)
    tilt(g, w, h)
    g = rotate_cw(g,w,h)
    tilt(g, h, w)
    g = rotate_cw(g,h,w)
    tilt(g, w, h)
    g = rotate_cw(g,w,h)
    return g

def pr(g,h,w):
    for r in range(h):
        for c in range(w):
            print(g[r,c],end='')
        print()
    print()

def sr(g,h,w):
    s = ''
    for r in range(h):
        for c in range(w):
            s+=g[r,c]
        s+='\n'
    return s

def load(g,h,w):
    acc = 0
    for r in range(h):
        for c in range(w):
            if g[r,c] == 'O':
                acc += h-r
    return acc

def solve():
    g = {}
    for r, row in enumerate(inp.splitlines()):
        h=r+1
        for c, col in enumerate(row):
            w=c+1
            g[r,c] = col

    pr(g,h,w)
    tilt(g,h,w)
    pr(g,h,w)
    acc = 0
    for r in range(h):
        for c in range(w):
            if g[r,c] == 'O':
                acc += h-r
    print(acc)

    print(2)
    g = defaultdict(lambda: '.')
    for r, row in enumerate(inp.splitlines()):
        h=r+1
        for c, col in enumerate(row):
            w=c+1
            g[r,c] = col

    # cycle find?
    cache = {}
    i = 0
    while True:
        print(i)
        s = sr(g,h,w)
        if s in cache:
            j = cache[s]
            break
        cache[s] = i
        g = cycle(g,h,w)
        print(i, load(g,h,w))
        i += 1
    print(i, j, 'same')
    print(j+(1000000000-i)%(i-j)-1)

if __name__ == '__main__':
    solve()
