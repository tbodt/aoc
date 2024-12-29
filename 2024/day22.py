import aoc
from collections import *
import re

inp='''1
2
3
2024
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def step(n):
    n = (n ^ (n<<6)) & 0xffffff
    n = (n ^ (n>>5)) & 0xffffff
    n = (n ^ (n<<11)) & 0xffffff
    return n

def find_cycle(f, n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = f(n)
    return len(seen)

streams = []
#acc = 0
for n in map(int,inp.splitlines()):
    stream = []
    for _ in range(2000):
        last = n
        n = step(n)
        stream.append((n%10, n%10 - last%10))
    streams.append(stream)
    #acc += n

def solve():
    print(sum(s[-1][0] for s in streams))
    possible_bananas = defaultdict(dict)
    for si, s in enumerate(streams):
        for i in range(4, len(s)):
            changes = tuple(a[1] for a in s[i-4:i])
            possible_bananas[changes].setdefault(si, s[i-1][0])
    #print(possible_bananas)
    changes, bananas = max(possible_bananas.items(), key=lambda a:sum(b for b in a[1].values()))
    print(changes, bananas, sum(bananas.values()))

def list_find(l, a):
    for i in range(len(l)-len(a)):
        if l[i:i+len(a)] == a:
            return i
    raise ValueError

if __name__ == '__main__':
    solve()
