import aoc
from collections import *
import re

inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def solve():
    g = {}
    for l in inp.splitlines():
        v, a = l.split(': ')
        a = a.split()
        g.setdefault(v, [])
        g[v].extend(a)
        for aa in a:
            g.setdefault(aa, [])
            g[aa].append(v)

    # with open('day25.dot', 'w') as f:
    #     print('graph {', file=f)
    #     for k, vv in g.items():
    #         for v in vv:
    #             print(k + '--' + v + ';', file=f)
    #     print('}', file=f)


    cut = [
        ("vgf","jpn"),
        ("fdb","txm"),
        ("nmz","mnl"),
    ]
    for a, b in cut:
        g[a].remove(b)
        g[b].remove(a)

    print(len(g), len(set(x for y in g.values() for x in y)))

    half = set()
    q = deque()
    q.append(next(iter(g.keys())))
    while q:
        a = q.popleft()
        if a in half: continue
        half.add(a)
        for adj in g[a]: q.append(adj)
    print(len(half), len(g)-len(half), len(half)*(len(g)-len(half)))

if __name__ == '__main__':
    solve()
