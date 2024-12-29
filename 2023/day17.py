import aoc
import random
import functools
from collections import *
import re

inp='''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

DIRS = [(0,1),(1,0),(0,-1),(-1,0)]
E,S,W,N = DIRS

TURN = {
    'L': {
        N:W,W:S,S:E,E:N,
    },
    'R': {
        N:E,E:S,S:W,W:N,
    },
}

g = {}
w = len(inp.splitlines())
h = len(inp.splitlines()[0])
for r, rr in enumerate(inp.splitlines()):
    for c, cc in enumerate(rr):
        g[r,c] = int(cc)

@functools.cache
def adj(at, face):
    heat_on_path = 0
    next_at = at
    steps = []
    a = []
    for dist in range(1,4):
        next_at = (next_at[0]+face[0], next_at[1]+face[1])
        steps.append(next_at)
        if next_at not in g: break
        heat_on_path += g[next_at]
        for turn in 'LR':
            next_face = TURN[turn][face]
            a.append((heat_on_path, steps, (next_at, next_face)))
    return a

@functools.cache
def ultra_adj(at, face):
    heat_on_path = 0
    next_at = at
    steps = []
    a = []
    for dist in range(1, 11):
        next_at = (next_at[0]+face[0], next_at[1]+face[1])
        steps.append(next_at)
        if next_at not in g: break
        heat_on_path += g[next_at]
        if dist < 4: continue
        for turn in 'LR':
            next_face = TURN[turn][face]
            a.append((heat_on_path, steps, (next_at, next_face)))
    return a

cache = {}
def path(at, face):
    if at == (h-1,w-1): return 0, []
    if (at, face) in cache: return cache[at, face]
    best_heat_try = (float('inf'), [])
    cache[at, face] = best_heat_try
    # six things to try
    steps = []
    for heat_on_path, steps, (next_at, next_face) in adj(at, face):
        p_heat, p = path(next_at, next_face)
        heat_try = heat_on_path + p_heat, steps + p
        best_heat_try = min(best_heat_try, heat_try)
    cache[at, face] = best_heat_try
    return best_heat_try

def solve():
    # best_heat, best_path = (path((0,0),DIRS[0]))
    # print(best_heat)
    # for r in range(h):
    #     for c in range(w):
    #         if (r,c) in best_path:
    #             print('*',end='')
    #         else:
    #             print(g[r,c],end='')
    #     print()

    # q = set()
    # done = set()
    # global results
    # start = ((0,0),DIRS[0])
    # results = {start: (0, [])}
    # q.add(start)
    # while q:
    #     _, x = min((results[x][0], x) for x in q)
    #     q.remove(x)
    #     done.add(x)
    #     p_heat, p = results[x]
    #     for heat_on_path, steps, y in adj(*x):
    #         if y in done: continue
    #         alt = p_heat + heat_on_path, p + steps
    #         results[y] = min(results.get(y, (float('inf'), [])),alt)
    #         q.add(y)
    # print(min(results[(h-1,w-1),d] for d in DIRS))

    q = set()
    done = set()
    global results
    start = ((0,0),DIRS[0])
    results = {start: (0, [])}
    q.add(start)
    while q:
        _, x = min((results[x][0], x) for x in q)
        q.remove(x)
        done.add(x)
        p_heat, p = results[x]
        for heat_on_path, steps, y in ultra_adj(*x):
            if y in done: continue
            alt = p_heat + heat_on_path, p + steps
            results[y] = min(results.get(y, (float('inf'), [])),alt)
            q.add(y)
    best_heat, best_path = min(results[(h-1,w-1),d] for d in DIRS)
    for r in range(h):
        for c in range(w):
            if (r,c) in best_path:
                print('*',end='')
            else:
                print(g[r,c],end='')
        print()
    print(best_heat, best_path)


if __name__ == '__main__':
    solve()
