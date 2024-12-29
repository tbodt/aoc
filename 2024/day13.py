import aoc
import z3
from collections import *
import re

inp='''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def solve():
    machines = []
    for m in inp.split('\n\n'):
        m=m.splitlines()
        ax, ay = map(int,re.findall(r'\+(\d+)', m[0]))
        bx, by = map(int,re.findall(r'\+(\d+)', m[1]))
        px, py = map(int,re.findall(r'=(\d+)', m[2]))
        machines.append(((ax,ay),(bx,by),(px,py)))
    acc=0
    for a, b, p in machines:
        #print(a,b,p)
        mintokens = float('inf')
        MAX = 100
        for na in range(MAX):
            for nb in range(MAX):
                if (a[0]*na+b[0]*nb == p[0] and a[1]*na+b[1]*nb == p[1]):
                    tokens = na*3+nb
                    if tokens < mintokens:
                        mintokens=tokens
        #print(mintokens)
        if mintokens != float('inf'):
            acc+=mintokens
    print(acc)

    acc=0
    for a, b, p in machines:
        print(a,b,p)
        p = p[0]+10000000000000,p[1]+10000000000000
        na = z3.Int('na')
        nb = z3.Int('nb')
        s = z3.Optimize()
        s.add(z3.And(a[0]*na+b[0]*nb == p[0], a[1]*na+b[1]*nb == p[1]))
        s.add(na>=0)
        s.add(nb>=0)
        tokens = na*3+nb
        s.minimize(tokens)
        if s.check() == z3.unsat: continue
        print(s.model())
        acc += s.model().evaluate(tokens).as_long()
    print(acc)

if __name__ == '__main__':
    solve()
