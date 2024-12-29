from collections import *
import pprint
import re

inp='''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
with open('input10.txt') as f: inp = f.read()

def addp(a, b):
    return tuple(a[i]+b[i] for i in range(len(a)))
DIRS=[(0,1),(0,-1),(1,0),(-1,0)]

def solve():
    g = {}
    for r, l in enumerate(inp.splitlines()):
        h = r
        for c, a in enumerate(l):
            g[r,c]=int(a)
            w = c

    trailheads = [p for p, level in g.items() if level == 0]
    print(trailheads)

    def head_trails(head, next=1):
        if next == 10:
            return (head, None)
        ts = []
        for d in DIRS:
            neigh = addp(head,d)
            if g.get(neigh) == next:
                ts.append(head_trails(neigh, next+1))
        return head, ts

    def ends(trail):
        s = set()
        def _e(trail,s):
            pt, children = trail
            if children is None: s.add(pt)
            else:
                for c in children: _e(c,s)
        _e(trail,s)
        return s

    def trail_score(ts):
        _, children = ts
        if children is None: return 1
        return sum(trail_score(a) for a in children)

    trails = [head_trails(h) for h in trailheads]
    pprint.pprint(trails[0])
    ends = [ends(t) for t in trails]
    print(ends, len(ends[0]))
    print(sum(len(e) for e in ends))
    scores = [trail_score(t) for t in trails]
    print(sum(scores), scores)

if __name__ == '__main__':
    solve()
