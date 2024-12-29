import aoc
import functools
from collections import *
import re

inp='''125 17'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def blink(stones):
    ss = []
    for s in stones:
        if s == 0:
            ss.append(1)
        elif len(str(s)) % 2 == 0:
            s = str(s)
            ss.append(int(s[:len(s)//2]))
            ss.append(int(s[len(s)//2:]))
        else:
            ss.append(s*2024)
    return ss

@functools.lru_cache(maxsize=None)
def size_after(s, steps):
    if steps == 0: return 1
    steps -= 1
    if s == 0:
        s = 1
        return size_after(s, steps)
    if len(str(s)) % 2 == 0:
        s = str(s)
        s1 = (int(s[:len(s)//2]))
        s2 = (int(s[len(s)//2:]))
        return size_after(s1, steps) + size_after(s2, steps)
    s = s * 2024
    return size_after(s, steps)

def solve():
    stones = [int(x) for x in inp.split()]
    N=75
    # for i in range(N):
    #     stones = blink(stones)
    #     print(i, len(stones))
    # print(len(stones))

    stones = [int(x) for x in inp.split()]
    print(sum(size_after(x, N) for x in stones))

if __name__ == '__main__':
    solve()
