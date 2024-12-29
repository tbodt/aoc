import aoc
import functools
from collections import *
import re

inp='''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

rules, updates = inp.split('\n\n')
after = defaultdict(list)
for r in rules.splitlines():
    first, second = map(int,r.split('|'))
    after[first].append(second)

def cmp(a, b):
    if a == b: return 0
    if b in after[a]: return 1
    if a in after[b]: return -1
    raise

def solve():
    s = 0
    for u in updates.splitlines():
        u = [int(a) for a in u.split(',')]
        for i in range(len(u)-1):
            if cmp(u[i],u[i+1]) != 1:
                break
        else:
            print(u)
            s += u[len(u)//2]
    print(s)

    s = 0
    for u in updates.splitlines():
        u = [int(a) for a in u.split(',')]
        print(u)
        for i in range(len(u)-1):
            if cmp(u[i],u[i+1]) != 1:
                print('bad')
                u.sort(key=functools.cmp_to_key(cmp))
                print(u, u[len(u)//2])
                s+= u[len(u)//2]
                break
    print(s)

if __name__ == '__main__':
    solve()
