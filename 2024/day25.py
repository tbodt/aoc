import aoc
from collections import *
import re

inp='''#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])
keys = []
locks = []
for shape in inp.split('\n\n'):
    ty = 'key' if shape[0] != '#' else 'lock'
    grid = shape.splitlines()
    pat = []
    for nc in range(len(grid[0])):
        col = [grid[r][nc] for r in range(len(grid))]
        pat.append(col.count('#')-1)
    if shape[0] == '#': locks.append(pat)
    else: keys.append(pat)

def solve():
    acc = 0
    for lock in locks:
        for key in keys:
            print(lock,key,[key[i] + lock[i] for i in range(len(key))])
            acc += not any(key[i] + lock[i] > 5 for i in range(len(key)))
    print(acc)

if __name__ == '__main__':
    solve()
