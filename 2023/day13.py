import aoc
import pprint
from collections import *
import re

inp='''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def transpose(thing):
    return [''.join(thing[r][c] for r in range(len(thing))) for c in range(len(thing[0]))]

def solve_horizontal(thing, smudge=False):
    for r in range(1,len(thing)):
        h1 = thing[:r]
        h2 = thing[r:]
        #pprint.pprint((h1,h2))
        if len(h1) > len(h2):
            h1 = h1[len(h1)-len(h2):]
        elif len(h1) < len(h2):
            h2 = h2[:len(h1)]
        #pprint.pprint((h1,h2))

        h2 = h2[::-1]
        diffs = sum(h1[r][c] != h2[r][c] for r in range(len(h1)) for c in range(len(h1[0])))
        if not smudge and diffs == 0:
            return r
        if smudge and diffs == 1:
            return r

def solve_one(thing, smudge=False):
    thing = thing.splitlines()
    n = solve_horizontal(thing, smudge)
    if n is not None: return (n)*100
    thing = transpose(thing)
    n = solve_horizontal(thing, smudge)
    if n is not None: return (n)

def solve():
    acc = 0
    for thing in inp.split('\n\n'):
        n = solve_one(thing)
        # print(thing, n)
        # print()
        acc += n
    print(acc)

    acc = 0
    for thing in inp.split('\n\n'):
        n = solve_one(thing, smudge=True)
        acc += n
    print(acc)

if __name__ == '__main__':
    solve()
