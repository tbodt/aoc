import aoc
from collections import *
import re

inp='''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def addp(a, b):
    return tuple(a[i] + b[i] for i in range(len(a)))

DIRS = [(0,1),(1,0),(0,-1),(-1,0)]
R,D,L,U = DIRS
DIRNAMES = {'R':R,'L':L,'U':U,'D':D}

def solve():
    g = defaultdict(lambda: '.')
    p = (0,0)
    nasin = []
    weka = 0
    for l in inp.splitlines():
        dir, dist, color = l.split()
        dir = DIRNAMES[dir]
        dist = int(dist)
        g[p] = '#'
        weka += dist
        nasin.append(p)
        p = (p[0]+dir[0]*dist,p[1]+dir[1]*dist)
    minr = min(r for r,c in g)
    maxr = max(r for r,c in g)+1
    minc = min(c for r,c in g)
    maxc = max(c for r,c in g)+1
    for r in range(minr, maxr):
        for c in range(minc, maxc):
            print(g[r,c],end='')
        print()

    palisa = []
    for n in range(len(nasin)):
        palisa.append((nasin[n],nasin[(n+1)%len(nasin)]))
    print(palisa)

    acc = 0
    for p1, p2 in palisa:
        # o weka e sinpin
        if p1[1] == p2[1]: continue
        print(p1,p2)
        # o nanpa e suli anpa
        acc += (p1[1]-p2[1]) * p1[0]
    print(acc)

    print(acc+weka//2+1)

    nasin = []
    weka = 0
    for l in inp.splitlines():
        dir, dist, color = l.split()
        dist, dir = (int(color[2:7], 16), [R,D,L,U][int(color[7])])
        weka += dist
        nasin.append(p)
        p = (p[0]+dir[0]*dist,p[1]+dir[1]*dist)

    palisa = []
    for n in range(len(nasin)):
        palisa.append((nasin[n],nasin[(n+1)%len(nasin)]))
    print(palisa)

    acc = 0
    for p1, p2 in palisa:
        # o weka e sinpin
        if p1[1] == p2[1]: continue
        print(p1,p2)
        # o nanpa e suli anpa
        acc += (p1[1]-p2[1]) * p1[0]
    print(acc)

    print(acc+weka//2+1)

    # print(len(g))

    ## bfs
    #q = deque()
    #q.append(((minr+maxr)//2, (minc+maxc)//2))
    #inside = set()
    #inside.add(q[0])
    #while q:
    #    p = q.popleft()
    #    for d in DIRS:
    #        poka = addp(p, d)
    #        if g[poka] == '#': continue
    #        if poka in inside: continue
    #        inside.add(poka)
    #        q.append(poka)
    #    #print(len(q))
    #print(len(inside))

    #acc = 0
    #for r in range(minr, maxr):
    #    for c in range(minc, maxc):
    #        if (r,c) in inside or (r,c) in g:
    #            #print('#',end='')
    #            acc += 1
    #        else:
    #            pass
    #            #print('.',end='')
    #    #print()
    #print(acc)

    # for l in inp.splitlines():
    #     dir, dist, color = l.split()
    #     dist, dir = (int(color[2:7], 16) // 50000, [R,D,L,U][int(color[7])])
    #     print(dist,dir)

if __name__ == '__main__':
    solve()
