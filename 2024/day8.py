import aoc
import itertools
from collections import *
import re

inp='''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

g = {}
for r, line in enumerate(inp.splitlines()):
    for c, ch in enumerate(line):
        if ch != '.':
            g[r,c]=ch
h=len(inp.splitlines())
w=len(inp.splitlines()[0])
frq = defaultdict(list)
for pt in g:
    frq[g[pt]].append(pt)

def jump(p1, p2):
    return p2[0]+(p2[0]-p1[0]),p2[1]+(p2[1]-p1[1])

def jumps(p1, p2):
    d0, d1 = p2[0]-p1[0], p2[1]-p1[1]
    t = p2[0],p2[1]
    yield t
    while True:
        t = t[0]+d0,t[1]+d1
        yield t

def solve():
    antis = set()
    for pts in frq.values():
        for p1, p2 in itertools.combinations(pts,2):
            antis.add(jump(p1,p2))
            antis.add(jump(p2,p1))
    antis = set(a for a in antis if 0<=a[0]<h and 0<=a[1]<w)

    for r in range(h):
        for c in range(w):
            if (r,c) in antis:
                print('#',end='')
            else:
                print(g.get((r,c),'.'),end='')
        print()
    print(len(antis),antis)

    antis = set()
    for pts in frq.values():
        for p1, p2 in itertools.combinations(pts,2):
            for j in jumps(p1,p2):
                if not (0<=j[0]<h and 0<=j[1]<w): break
                antis.add(j)
            for j in jumps(p2,p1):
                if not (0<=j[0]<h and 0<=j[1]<w): break
                antis.add(j)

    print(len(antis),antis)
    antis = set(a for a in antis if 0<=a[0]<h and 0<=a[1]<w)
    print(len(antis),antis)

    for r in range(h):
        for c in range(w):
            if (r,c) in antis:
                print('#',end='')
            else:
                print(g.get((r,c),'.'),end='')
        print()
    print(len(antis),antis)


if __name__ == '__main__':
    solve()
