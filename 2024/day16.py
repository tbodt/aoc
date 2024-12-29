import aoc
from grid import *
from collections import *
import re

inp='''#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

def solve():
    g = {}
    for r, l in enumerate(inp.splitlines()):
        for c, ch in enumerate(l):
            if ch != '.':
                g[r,c] = ch
    inp.splitlines()
    start = next(k for k, v in g.items() if v == 'S')
    end = next(k for k, v in g.items() if v == 'E')
    del g[start]
    del g[end]

    dist = {}
    prev = {}
    q = set()
    q.add(start)
    dist[start] = 0
    while q:
        v = min(q, key=lambda a: dist.get(a, float('inf')))
        q.remove(v)
        prev_d = prev[v][1] if v != start else 1
        neigh = [
            (prev_d, 1),
            ((prev_d+1)%len(DIRS), 1001),
            ((prev_d-1)%len(DIRS), 1001),
        ]
        for dir, cost in neigh:
            n = addp(v, DIRS[dir])
            if g.get(n) == '#': continue
            total_cost = dist[v] + cost
            if n not in dist or total_cost < dist[n]:
                dist[n] = total_cost
                prev[n] = v, dir
                q.add(n)

    print(dist[end])
    print(prev[end])

    dist = {}
    prev = {}
    q = set()
    start = (start, 1)
    q.add(start)
    dist[start] = 0
    while q:
        v = min(q, key=lambda a: dist.get(a, float('inf')))
        print(v)
        q.remove(v)
        p, dir = v
        neigh = [
            ((addp(p, DIRS[dir]), dir), 1),
            ((p, (dir+1)%len(DIRS)), 1000),
            ((p, (dir-1)%len(DIRS)), 1000),
        ]
        for n, cost in neigh:
            if g.get(n[0]) == '#': continue
            total_cost = dist[v] + cost
            if n not in dist or total_cost < dist[n]:
                dist[n] = total_cost
                prev[n] = {v}
                q.add(n)
            if total_cost == dist.get(n):
                prev[n].add(v)

    end = min(((end,d) for d in range(len(DIRS))), key=lambda a: dist.get(a, float('inf')))
    print(end, dist[end])
    print(prev)

    stack = [end]
    covered_nodes = set()
    while stack:
        a = stack.pop()
        covered_nodes.add(a[0])
        if a in prev: stack.extend(prev[a])
    print(len(covered_nodes))

    for r in range(gheight(g)):
        for c in range(gwidth(g)):
            if (r,c) in covered_nodes:
                print('O',end='')
            else:
                print(g.get((r,c),'.'),end='')
        print()

if __name__ == '__main__':
    solve()
