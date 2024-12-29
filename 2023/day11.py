import aoc
from collections import *
import re

inp='''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def expand(universe, w, h, amount=1):
    empty_rows = []
    for r in range(h):
        if all((r,c) not in universe for c in range(w)):
            empty_rows.append(r)
    empty_cols= []
    for c in range(w):
        if all((r,c) not in universe for r in range(h)):
            empty_cols.append(c)
    u2 = {}
    xr = 0
    for r in range(h):
        xc = 0
        for c in range(w):
            crep = 1 if c not in empty_cols else 1+amount
            if (r,c) not in universe:
                xc += crep - 1
                continue
            xc -= 1
            for _ in range(crep):
                xc += 1
                u2[r+xr,c+xc] = universe[r,c]

        rrep = 0 if r not in empty_rows else amount
        xr += rrep

    return u2

def solve():
    g={}
    h = len(inp.splitlines())
    w = len(inp.splitlines()[0])
    for r, rr in enumerate(inp.splitlines()):
        for c, cc in enumerate(rr):
            if cc != '.':
                g[r,c] = cc

    u2 = expand(g, w, h)
    h2,w2 = max(r for r,c in u2), max(c for r,c in u2)
    h2,w2=h2+1,w2+1
    for r in range(h2):
        for c in range(w2):
            print(u2.get((r,c),'.'),end='')
        print()

    gs = list(u2)
    print(gs)
    acc=0
    for i, g1 in enumerate(gs):
        for g2 in gs[i+1:]:
            acc+= dist(g1,g2)
    print(acc)

    u3 = expand(g,w,h,amount=999999)
    h2,w2 = max(r for r,c in u3), max(c for r,c in u3)
    h2,w2=h2+1,w2+1
    # for r in range(h2):
    #     for c in range(w2):
    #         print(u3.get((r,c),'.'),end='')
    #     print()
    # print()

    gs = list(u3)
    print(gs)
    acc=0
    for i, g1 in enumerate(gs):
        for g2 in gs[i+1:]:
            acc+= dist(g1,g2)
    print(acc)


if __name__ == '__main__':
    solve()
