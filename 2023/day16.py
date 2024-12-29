import aoc
from collections import *
import re

inp=r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])


DIRS = [(0,1),(1,0),(0,-1),(-1,0)]
E,S,W,N = DIRS

MIRRORS = {
    '/': {
        S: W,
        W: S,
        N: E,
        E: N,
    },
    '\\': {
        S: E,
        W: N,
        N: W,
        E: S,
    },
    '|': {
        E: [N,S],
        W: [N,S],
        S: S,
        N: N,
    },
    '-': {
        S: [E,W],
        N: [E,W],
        E: E,
        W: W,
    },
}

def solve():
    g = inp.splitlines()
    w = len(g[0])
    h = len(g)
    g={}
    for r, rr in enumerate(inp.splitlines()):
        for c, cc in enumerate(rr):
            g[r,c] = cc

    for r in range(h):
        for c in range(w):
            print(g[r,c],end='')
        print()
    p = 0,0
    d = DIRS[0]
    hits = set()
    def fire(p, d):
        if (p,d) in hits: return
        while p in g:
            hits.add((p,d))
            if g[p] == '.':
                pass
            elif g[p] in '\\/-|':
                d = MIRRORS[g[p]][d]
                if isinstance(d, list):
                    for dd in d:
                        fire(p, dd)
                    break
            p = (p[0]+d[0],p[1]+d[1])
    fire((0,0),E)
    real_hits = {p:d for p,d in hits}
    for r in range(h):
        for c in range(w):
            print('.#'[(r,c) in real_hits], end='')
        print()
    print(len(real_hits))

    to_try = []
    for r in range(h):
        to_try.append(((r, 0), E))
        to_try.append(((r, w-1), W))
    for c in range(w):
        to_try.append(((0, c), S))
        to_try.append(((h-1, c), N))
    best = 0
    for t in to_try:
        hits = set()
        fire(*t)
        real_hits = {p:d for p,d in hits}
        print(t, len(real_hits))
        if len(real_hits) > best: best = len(real_hits)
    print(best)


if __name__ == '__main__':
    solve()
