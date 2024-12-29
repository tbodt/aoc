import aoc
from collections import *
import re

inp='''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

DIRS = [(1,0), (0,1), (-1,0), (0,-1)]
def addp(a, b):
    return tuple(a[i] + b[i] for i in range(len(a)))

CONNS = {
    '|': ((1,0),(-1,0)),
    '-': ((0,1),(0,-1)),
    'L': ((-1,0),(0,1)),
    'J': ((-1,0),(0,-1)),
    '7': ((1,0),(0,-1)),
    'F': ((1,0),(0,1)),
}

BOX = {
    '|': '│',
    '-': '─',
    'L': '└',
    'J': '┘',
    '7': '┐',
    'F': '┌',
}

def dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def solve():
    g=defaultdict(lambda: '.')
    h = len(inp.splitlines())
    w = len(inp.splitlines()[0])
    for r, rr in enumerate(inp.splitlines()):
        for c, cc in enumerate(rr):
            g[r,c] = cc
    start = next((r,c) for r,c in g if g[r,c] == 'S')
    for r in range(start[0]-1, start[0]+2):
        for c in range(start[1]-1, start[1]+2):
            print(g[r,c],end='')
        print()
    repl = '|'
    print(f'replacing start with {repl}!')
    g[start] = repl

    path = []
    path.append(start)
    while True:
        p = path[-1]
        nexts = [addp(p, c) for c in CONNS[g[p]]]
        n = next(n for n in nexts if len(path)<=1 or path[-2] != n)
        if n == start: break
        path.append(n)
    path.append(start)
    #print(path, len(path))
    p2=path[::-1]
    pdists = {}
    for i, p in enumerate(path):
        pdists[p] = min(i, len(path)-i)
    bdist = float('-inf')
    inside_count = 0
    for r in range(h):
        print(r, end=' ')
        for c in range(w):
            if (r,c) in pdists:
                dist = pdists[r,c]
                if dist > bdist: bdist=dist
                print(BOX[g[r,c]],end='')
            else:
                # is inside or out?
                #if (r,c) == (82,43):
                    #import ipdb;ipdb.set_trace()
                swaps = 0
                enter = None
                exit = None
                for fr in range(r, h+1):
                    if (fr,c) not in pdists: continue
                    pipe = g[fr,c]
                    if pipe == '-':
                        swaps += 1
                    elif pipe == '|':
                        pass
                    elif pipe == '7':
                        enter = 'L'
                    elif pipe == 'F':
                        enter = 'R'
                    elif pipe == 'L':
                        exit = 'R'
                    elif pipe == 'J':
                        exit = 'L'
                    if exit is not None:
                        if enter != exit:
                            swaps += 1
                        enter = None
                        exit = None
                    # J
                    # L
                if swaps % 2 == 1:
                    # inside
                    inside_count += 1
                    print('I',end='')
                else:
                    print('O',end='')
        print()
    print(bdist)
    print(inside_count)

if __name__ == '__main__':
    solve()
