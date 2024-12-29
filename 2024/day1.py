import aoc
from collections import *
import re

inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def solve():
    l = []
    r = []
    for ln in inp.splitlines():
        n1, n2 = map(int,ln.split())
        l.append(n1)
        r.append(n2)
    l.sort()
    r.sort()
    s=0
    for a, b in zip(l,r):
        s+=abs(a-b)
    print(s)

    s=0
    for n in l:
        s+=n*r.count(n)
    print(s)

if __name__ == '__main__':
    solve()
