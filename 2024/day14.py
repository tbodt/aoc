from collections import *
import pprint
import re

def addp(a, b):
    return tuple(a[i]+b[i] for i in range(len(a)))

inp='''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''
w,h=11,7
with open('input14.txt') as f: inp = f.read()
w,h = 101,103

robots = []
for line in inp.splitlines():
    px,py,vx,vy = map(int,re.findall(r'(-?\d+)', line))
    robots.append(((px,py),(vx,vy)))

def robots_at_time(t):
    rs = defaultdict(int)
    for p, v in robots:
        p = ((p[0]+v[0]*t) % w, (p[1]+v[1]*t) % h)
        rs[p] += 1
    return rs

def pr(t):
    s = ''
    rs = robots_at_time(t)
    for r in range(h):
        for c in range(w):
            cnt = rs[c,r]
            s += str(cnt if cnt else '.')
        s += '\n'
    print(s)

def solve():
    final_robots = robots_at_time(100)
    q = [[0,0],[0,0]]
    for p, count in final_robots.items():
        if p[0] < w//2: q0 = 0
        elif p[0] > w//2: q0 = 1
        else: continue
        if p[1] < h//2: q1 = 0
        elif p[1] > h//2: q1 = 1
        else: continue
        q[q0][q1] += count
    print(q, q[0][0]*q[0][1]*q[1][0]*q[1][1])

    #153712375
    #80100 * 1919 + 475
    #69*1919+475

    # a * 1919 + 475 = t
    # b * 103 + 16 = t
    # t % 1919 = 475
    # t % 103 = 16 x


    for i in range(-10, 10):
        i = (i*103+69)*1919+475
        print(i)
        pr(i)
        import time;time.sleep(0.01)


if __name__ == '__main__':
    solve()
