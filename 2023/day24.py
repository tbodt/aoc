import aoc
import z3
from collections import *
import re

inp='''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def parse1(l):
    pos, vel = l.split(' @ ')
    pos = tuple(map(int,pos.split(', ')))
    vel = tuple(map(int,vel.split(', ')))
    return pos,vel

stones = []
for l in inp.splitlines():
    stones.append(parse1(l))

def intersect_xy(stone1, stone2):
    # x = px + t*vx, y = py + t*vy
    # y - py = (vy/vx)(x - px)
    # y = (vy/vx)(x - px) + py
    # y = x*vy/vx - px*vy/vx + py
    # m[i] = vy[i]/vx[i]
    # m1*x - m1*px1 + py1 = m2*x - m2*px2 + py2
    # m1*x - m2*x = - m2*px2 + py2 + m1*px1 - py1
    # (m1-m2)*x = ^
    # x = (py2 - py1 + m1*px1 - m2*px2) / (m1 - m2)
    # y = x*m1 - px1*m1 + py1
    p1, v1 = stone1
    p2, v2 = stone2
    m1 = v1[1]/v1[0]
    m2 = v2[1]/v2[0]
    if m1 == m2: return None
    x = (p2[1]-p1[1]+m1*p1[0]-m2*p2[0])/(m1-m2)
    y = x*m2-p2[0]*m2+p2[1]

    # in past?
    # x = px + t*vx, y = py + t*vy
    # (x - px) / vx = t
    t1 = (x - p1[0]) / v1[0]
    t2 = (x - p2[0]) / v2[0]
    if t1 < 0 or t2 < 0: return None
    return x,y

def solve():
    acc=0
    for i in range(len(stones)):
        for j in range(i+1, len(stones)):
            isect = intersect_xy(stones[i], stones[j])
            if isect is None: continue
            x,y=isect
            #print(stones[i], stones[j], x,y)
            if all(200000000000000<=a<=400000000000000 for a in (x,y)):
                acc +=1


    # ok big system of equations
    # 6 unknowns, each line 1 new unknown and 3 equations, x*3 = 6+x, three lines? nine equations, nine unknowns
    # ?px + ?vx*?t1 = p1x + v1x*t1
    # ?py + ?vy*?t1 = p1y + v1y*t1
    # ?pz + ?vz*?t1 = p1z + v1z*t1
    # px + vx*t2 = p2x + v2x*t2
    # p_d + v_d*t_n = p_n_d + v_n_d*t_n
    # ?p_d + (?v_d - v_n_d)*?t_n = p_n_d
    print(acc)
    s = z3.Solver()
    dim_names = 'xyz'
    p = [z3.Int('p'+dim_names[i]) for i in range(3)]
    v = [z3.Int('v'+dim_names[i]) for i in range(3)]
    ts = [z3.Int('t'+str(i)) for i in range(len(stones))]
    for i in range(len(stones)):
        s.add(ts[i] >= 0)
    for dim in range(3):
        ps = [s[0][dim] for s in stones]
        vs = [s[1][dim] for s in stones]
        for i in range(len(stones)):
            s.add(p[dim] + v[dim]*ts[i] == ps[i] + vs[i]*ts[i])
    print(s)
    print(s.check())
    print([s.model()[var] for var in p+v])

if __name__ == '__main__':
    solve()
