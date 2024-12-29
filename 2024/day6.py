import aoc
from collections import *
import re

inp='''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

DIRS = [(-1,0), (0,1), (1,0), (0,-1)]
def addp(a, b):
    return tuple(a[i] + b[i] for i in range(len(a)))

def solve():
    g = {}
    for r, l in enumerate(inp.splitlines()):
        for c, a in enumerate(l):
            g[r,c]=a
    h = len(inp.splitlines())
    w = len(inp.splitlines()[0])
    guard = next((r,c) for r in range(h) for c in range(w) if g[r,c]=='^')
    dir = 0
    path = [(guard,dir)]

    def dump():
        for r in range(h):
            for c in range(w):
                if (r,c) in path: print('X',end='')
                else: print(g[r,c],end='')
            print()

    while True:
        guard,dir=path[-1]
        n = addp(guard, DIRS[dir])
        if n not in g: break
        if g[n] != '#':
            guard = n
        else:
            dir = (dir + 1) % len(DIRS)
        path.append((guard,dir))
        #print(guard, dir, path)
        #dump()
        #print()
    points = set(p for p,d in path)
    print(len(points))

    first_seen = {}
    for i, (p, d) in enumerate(path):
        if i ==0:continue
        first_seen.setdefault(p, i)
    loops = 0
    for p, i in sorted(first_seen.items(),key=lambda a:a[1]):
        g[p] = '#'
        so_far = path[0:i]
        print(p,i)
        seen = set()
        while True:
            guard,dir=so_far[-1]
            n = addp(guard, DIRS[dir])
            if n not in g:
                loop = False
                break
            if g[n] != '#':
                guard = n
            else:
                dir = (dir + 1) % len(DIRS)
            if (guard,dir) in seen:
                loop = True
                break
            so_far.append((guard,dir))
            seen.add((guard,dir))
        loops += loop
        g[p] = '.'
    print(loops)

if __name__ == '__main__':
    solve()
