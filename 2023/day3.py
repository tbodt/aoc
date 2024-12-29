import aoc
from collections import *
import re

inp='''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def solve():
    ll = list(inp.splitlines())
    g = {}
    for r,a in enumerate(ll):
        for c,x in enumerate(a):
            g[r,c] = x
    print(g)

    def hassym(a): return any(b != '.' and not b.isdigit() for b in a)

    tot = 0
    for r,a in enumerate(ll):
        for n in re.finditer('\d+',a):
            print(n.group(), n.start(0))
            cstart = n.start(0)
            cend = n.end(0)
            sym = False
            poka = []
            if r - 1 >= 0:
                poka.append(ll[r-1][max(n.start(0)-1,0):min(n.end(0)+1,len(a))])
            if r + 1 < len(ll):
                poka.append(ll[r+1][max(n.start(0)-1,0):min(n.end(0)+1,len(a))])
            if cstart - 1 >= 0:
                poka.append(a[cstart-1])
            if cend < len(a):
                poka.append(a[cend])
            print(poka)
            print(any(hassym(x) for x in poka))
            if not (any(hassym(x) for x in poka)): continue
            tot += int(n.group())
            #if r-1 >= 0: sym = sym or hassym(ll[r-1][n.start(0):n.end(0)])
    print(tot)

def solve2():
    ll = list(inp.splitlines())
    g = {}
    for r,a in enumerate(ll):
        for c,x in enumerate(a):
            g[r,c] = x
    print(g)

    gears = defaultdict(list)

    tot = 0
    for r,a in enumerate(ll):
        for n in re.finditer('\d+',a):
            print(n.group(), n.start(0))
            cstart = n.start(0)
            cend = n.end(0)
            sym = False
            poka = []
            for gr in (r-1,r,r+1):
                for gc in range(cstart-1, cend+1):
                    if gr <= 0 or gc <= 0 or gr >= len(ll) or gc >= len(a): continue
                    ch = ll[gr][gc]
                    if ch != '.' and not ch.isdigit():
                        gears[gr,gc].append(int(n.group()))
    print(gears)
    for g in gears.values():
        if len(g) != 2: continue
        print(g[0]*g[1])
        tot += g[0]*g[1]
    print(tot)

if __name__ == '__main__':
    #solve()
    solve2()
