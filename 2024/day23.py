import aoc
from collections import *
import re

inp='''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

edges = [tuple(l.split('-')) for l in inp.splitlines()]
adj = defaultdict(set)
for e1, e2 in edges:
    adj[e1].add(e2)
    adj[e2].add(e1)
verts = list(adj)

def dot():
    print('graph {')
    for src, dst in edges:
        print(f'{src} -- {dst};');
    print('}')


def union(regions, a, b):
    members = set()
    if a in regions: members.update(regions[a])
    if b in regions: members.update(regions[b])
    members.add(a)
    members.add(b)
    for m in members: regions[m] = members

def solve():
    cycles = set()
    for v in verts:
        if not v.startswith('t'): continue
        print(v)
        for v2 in adj[v]:
            for v3 in adj[v2]:
                if v in adj[v3]:
                    c = [v, v2, v3]
                    c.sort()
                    cycles.add(tuple(c))
    print(len(cycles))

adjself = {k: v | {k} for k,v in adj.items()}
def solve2():
    groups = {}
    for v in verts:
        commons = defaultdict(set)
        for v2 in verts:
            common = adjself[v].intersection(adjself[v2])
            if len(common) != len(adj[v]): continue
            commons[tuple(sorted(common))].add(v)
            commons[tuple(sorted(common))].add(v2)
        if commons:
            print(v, sorted(next(iter(commons.values()))))

if __name__ == '__main__':
    solve()
    solve2()
