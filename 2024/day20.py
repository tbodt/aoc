import aoc
import pprint
from grid import *
from collections import *
import re

inp='''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])
g = {}
for r, l in enumerate(inp.splitlines()):
    for c, ch in enumerate(l):
        if ch == 'S': start = (r,c)
        if ch == 'E': end = r,c
        if ch == '#': g[r,c]=ch
DIRS=[(0,1),(1,0),(0,-1),(-1,0)]

def dists_from(g, start):
    q = deque()
    from_start = {}
    q.append(start)
    from_start[start] = 0
    while q:
        a = q.popleft()
        for d in DIRS:
            nei = addp(a, d)
            if nei in g: continue
            if nei not in from_start:
                from_start[nei] = from_start[a] + 1
                q.append(nei)
    return from_start

from_start = dists_from(g, start)
from_end = dists_from(g, end)

# ..x..
# .x.x.
# x.o.x
# .x.x.
# ..x..

def two_moves(p):
    for r in range(-2,+3):
        for c in range(-2,+3):
            if abs(r)+abs(c) == 2:
                yield addp(p, (r,c))

def moves_of_size(size):
    for r in range(-size,+size+1):
        for c in range(-size,+size+1):
            if abs(r)+abs(c) <= size:
                yield (r,c)


def solve():
    SIZE = 2

    cnt = Counter()
    for p in from_start:
        for m in moves_of_size(SIZE):
            mp = addp(p, m)
            msize = abs(m[0])+abs(m[1])
            if mp in from_end:
                length = from_start[p] + msize + from_end[mp]
                saved = from_end[start] - length
                if saved <= 0: continue
                #print(p, m, mp, length, saved)
                cnt[saved] += 1
    print(cnt)
    print(sum(c for save, c in cnt.items() if save >= 100))

    SIZE = 20

    cnt = Counter()
    for p in from_start:
        for m in moves_of_size(SIZE):
            mp = addp(p, m)
            msize = abs(m[0])+abs(m[1])
            if mp in from_end:
                length = from_start[p] + msize + from_end[mp]
                saved = from_end[start] - length
                if saved <= 0: continue
                print(p, m, mp, length, saved)
                cnt[saved] += 1
    print(cnt)
    print(sum(c for save, c in cnt.items() if save >= 100))

if __name__ == '__main__':
    solve()
