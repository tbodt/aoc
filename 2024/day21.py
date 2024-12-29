import aoc
import functools
from collections import *
import re

inp='''029A
980A
179A
456A
379A
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

digits = [['7','8','9'],['4','5','6'],['1','2','3'],[None,'0','A']]
dirs = [[None,'^','A'],['<','v','>']]
def make_adj(grid):
    adj = {}
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            a = grid[r][c]
            if a is None: continue
            adj[a] = {}
            if 0 <= r+1 < len(grid): adj[a]['v'] = grid[r+1][c]
            if 0 <= r-1 < len(grid): adj[a]['^'] = grid[r-1][c]
            if 0 <= c+1 < len(grid[0]): adj[a]['>'] = grid[r][c+1]
            if 0 <= c-1 < len(grid[0]): adj[a]['<'] = grid[r][c-1]
            adj[a] = {d:a for d,a in adj[a].items() if a is not None}
    return adj
digits = make_adj(digits)
dirs = make_adj(dirs)
KEYPADS = (dirs, dirs, digits)

def all_shortest_paths(start, end, adj):
    q = deque()
    q.append(start)
    last = {start: (0, [])}
    while q:
        a = q.popleft()
        dist, ways_back = last[a]
        for dir, b in adj[a].items():
            if b not in last: q.append(b)
            if b not in last or last[b][0] > dist+1:
                last[b] = (dist+1, [])
            if last[b][0] == dist+1:
                last[b][1].append((dir, a))
    def collect_paths(to):
        dist, prevs = last[to]
        if not prevs:
            yield ''
            return
        for dir, prev in prevs:
            for prev_path in collect_paths(prev):
                yield prev_path + dir
    return list(collect_paths(end))
all_digit_paths = {d1: {d2: all_shortest_paths(d1, d2, digits) for d2 in digits} for d1 in digits}
all_dir_paths = {d1: {d2: all_shortest_paths(d1, d2, dirs) for d2 in dirs} for d1 in dirs}


@functools.lru_cache
def shortest_to_enter_pattern(pattern, extra_keypads, keypad='digits'):
    #print(extra_keypads, pattern)
    pos = 'A'
    shortest = ''
    keypad_paths = {'digits': all_digit_paths, 'dirs': all_dir_paths}[keypad]
    for key in pattern:
        paths = keypad_paths[pos][key]
        if extra_keypads == 0:
            shortest += paths[0] + 'A'
        else:
            shortest += min((shortest_to_enter_pattern(p + 'A', extra_keypads-1, 'dirs') for p in paths), key=len)
        pos = key
    return shortest

@functools.lru_cache
def fewest_to_enter_pattern(pattern, extra_keypads, keypad='digits'):
    #print(extra_keypads, pattern)
    pos = 'A'
    fewest = 0
    keypad_paths = {'digits': all_digit_paths, 'dirs': all_dir_paths}[keypad]
    for key in pattern:
        paths = keypad_paths[pos][key]
        if extra_keypads == 0:
            fewest += len(paths[0]) + len('A')
        else:
            fewest += min(fewest_to_enter_pattern(p + 'A', extra_keypads-1, 'dirs') for p in paths)
        pos = key
    return fewest

def solve():
    codes = inp.splitlines()
    acc=0
    for code in codes:
        fewest = fewest_to_enter_pattern(code, 2)
        print(code, fewest)
        acc += int(code[:3])*fewest
    print(acc)

if __name__ == '__main__':
    solve()
