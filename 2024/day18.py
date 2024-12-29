import aoc
from collections import *
import re
from grid import *

inp = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
'''
size=7
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1]); size=71
g = {}
for i, p in enumerate(inp.splitlines()):
    x,y = map(int,p.split(','))
    g[y,x] = i

DIRS=[(0,1),(1,0),(-1,0),(0,-1)]

def solve():
    def with_first_n(firstn):
        start = 0,0
        end=size-1,size-1
        q = deque()
        q.append(start)
        prev = {start:None}
        while q:
            here = q.popleft()
            for d in DIRS:
                n = addp(here, d)
                if not (0 <= n[0] < size and 0 <= n[1] < size): continue
                if n in g and g[n] < firstn: continue
                if n in prev: continue
                prev[n] = here
                #print(here, '->', n)
                q.append(n)
        cnt = 0
        p = end
        while prev[p]:
            cnt += 1
            p = prev[p]
        return cnt
    for i in range(len(inp.splitlines())):
        print(i, with_first_n(i))

if __name__ == '__main__':
    solve()
