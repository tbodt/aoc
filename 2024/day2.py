import aoc
from collections import *
import re

inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])
inp='''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''

def sign(x):
    return x/abs(x) if x else 0

def safe(l):
    s = None
    for i in range(len(l)-1):
        diff = l[i]-l[i+1]
        if not (1 <= abs(diff) <= 3):
            return False
        if s is not None:
            if s != sign(diff):
                return False
        else:
            s = sign(diff)
    return True

def solve():
    s=0
    for l in inp.splitlines():
        l = list(map(int,l.split()))
        print(l, safe(l))
        if safe(l):
            s += 1
    print(s)

    s=0
    for l in inp.splitlines():
        l = list(map(int,l.split()))
        cansafe = False
        for ti in range(len(l)):
            l2 = list(l)
            del l2[ti]
            cansafe = cansafe or safe(l2)
        print(l, cansafe)
        if cansafe:
            s += 1
    print(s)

if __name__ == '__main__':
    solve()
