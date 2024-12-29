import aoc
import grid
from collections import *
import re

inp='''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

def perp(dir):
    return (abs(dir[1]), abs(dir[0])), (-abs(dir[1]), -abs(dir[0]))

def solve():
    g = {}
    for r, l in enumerate(inp.splitlines()):
        for c, ch in enumerate(l):
            g[r,c]=ch
            w = c+1
        h = r+1

    regions = {}
    def union(a, b):
        members = set()
        if a in regions: members.update(regions[a])
        if b in regions: members.update(regions[b])
        members.add(a)
        members.add(b)
        for m in members: regions[m] = members

    for r in range(h):
        for c in range(w):
            p=(r,c)
            regions.setdefault(p, {p})

    for r in range(h):
        for c in range(w):
            p=(r,c)
            color = g[p]
            for d in DIRS:
                neigh = grid.addp(p,d)
                if g.get(neigh) == color:
                    union(p, neigh)

    seen = set()
    rs=[]
    for r in regions.values():
        if id(r) in seen: continue
        seen.add(id(r))
        #print(r, g[next(iter(r))])
        rs.append(r)
    print(len(rs))

    perim = defaultdict(int)
    area = defaultdict(int)
    for r in range(h):
        for c in range(w):
            p=(r,c)
            color = id(regions[p])
            area[color] += 1
            for d in DIRS:
                neigh = grid.addp(p,d)
                if neigh not in regions or color != id(regions[neigh]):
                    perim[color] += 1
    #print(acc)
    acc = 0
    for r in perim:
        acc += perim[r] * area[r]
    print(acc)

    #2
    acc = 0
    for r in rs:
        #if g[next(iter(r))] != 'M': continue
        print(r)
        edges = set()
        for p in r:
            for d in DIRS:
                neigh = grid.addp(p, d)
                if neigh not in r:
                    edges.add((p, d))
        #print(len(edges))
        #print(edges)
        assert len(edges) == perim[id(r)]
        #import ipdb;ipdb.set_trace()
        for e in list(edges):
            if e not in edges: continue
            pt, dir = e
            pd1, pd2 = perp(dir)
            p = grid.addp(pt, pd1)
            while (p, dir) in edges:
                edges.remove((p, dir))
                #print(e, (p, dir))
                p = grid.addp(p, pd1)
            p = grid.addp(pt, pd2)
            while (p, dir) in edges:
                #print(e, (p, dir))
                edges.remove((p, dir))
                p = grid.addp(p, pd2)
        #print(edges)
        print(g[next(iter(r))], area[id(r)], len(edges), len(edges)*area[id(r)])
        acc += len(edges)*area[id(r)]
    print(acc)

if __name__ == '__main__':
    solve()
