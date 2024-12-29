import aoc
import time
from collections import *
import re

inp='''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

DIRS = [(0,1),(1,0),(0,-1),(-1,0)]

def addp(a, b):
    return tuple(a[i] + b[i] for i in range(len(a)))

#def count_with_parity_in_radius(rad, par):
#    acc = 0
#    for r in range(-rad,rad+1):
#        for c in range(-rad,rad+1):
#            if r+c > rad: continue
#            if (r+c)%2 == par: acc += 1
#    sq = (rad*2+1)**2
#    sq //= 2
#    #if par == 0: sq += 1
#    assert sq == acc, f'{sq} {acc}'
#    return sq
#    # 4r + 4(r-1) + 4(r-2)
#    # 4(r+(r-1)+(r-2))
#    # n + (n-1) + (n-2)
#    # n = m * 2

def solve():
    g = {}
    for r, rr in enumerate(inp.splitlines()):
        for c, cc in enumerate(rr):
            if cc == 'S':
                cc = '.'
                start = (r,c)
            g[r,c]=cc

    h = len(inp.splitlines())
    w = len(inp.splitlines()[0])


    def box(pp):
        return (pp[0]%h, pp[1]%w)
    def adj_inf(p):
        for d in DIRS:
            pp = addp(p,d)
            if g[box(pp)] == '#': continue
            yield pp

    def adj(p):
        for d in DIRS:
            pp = addp(p,d)
            if pp not in g: continue
            if g[pp] == '#': continue
            yield pp

    N = 1000
    at = set([start])
    for i in range(N):
        at_sin = set()
        for p in at:
            for a in adj_inf(p):
                at_sin.add(a)
        at = at_sin
        S = 3
        if (i+1)%131 == 65:
            print(i+1,',',len(at))
        # if i%2 == 0:
        #     for a in at:
        #         assert (abs(a[0])+abs(a[1])) %2 == 1
        # for r in range(h*(-S+1),h*S):
        #     for c in range(w*(-S+1),w*S):
        #         if (r,c) in at:
        #             print('O',end='')
        #         else:
        #             print(g[box((r,c))],end='')
        #     print()
        # time.sleep(0.05)
    print(i, len(at))

# But first, we have to talk about parallel universes.

    # radius = 100
    # USIZE = w*2
    # universe_radius = radius // USIZE
    # for ur in range(-universe_radius-10, universe_radius+10):
    #     for uc in range(universe_radius - kkkkkkkkkkkkkkkkkkkkk
    #     # startr + ?r + startc + ?c == radius
    #     # r = ur*USIZE + ?dr
    #     # c = uc*USIZE + ?dc
    #     # startr + ur*USIZE + ?dr + startc + ?c == radius
    #     # startr + ur*USIZE + startc - radius = - ?dr - uc*USIZE - ?dc == radius
    #     # startr + ur*USIZE + startc - radius = - ?dr - uc*USIZE - ?dc == radius
    #     # calculate uc such that taxicab(ur*USIZE+start[0], uc*USIZE+start[1]) == radius
    #     # ur*USIZE + startr + uc*USIZE + startc == radius
    #     # ur + uc == 

if __name__ == '__main__':
    solve()
