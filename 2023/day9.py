import aoc
from collections import *
import re

inp='''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def solve():
    vs = [[int(x) for x in y.split()] for y in inp.splitlines()]
    acc=0
    acc2=0
    for v1 in vs:
        ds = [v1]
        while True:
            dlast = ds[-1]
            dsin = []
            for i in range(1, len(dlast)):
                dsin.append(dlast[i] - dlast[i-1])
            ds.append(dsin)
            if all(x == 0 for x in dsin): break
        print(ds)

        for i in range(len(ds)-1,-1,-1):
            if i == len(ds)-1:
                ds[i].append(0)
                continue
            ds[i].append(ds[i][-1]+ds[i+1][-1])
        print(ds)

        for i in range(len(ds)-1,-1,-1):
            if i == len(ds)-1:
                ds[i].insert(0, 0)
                continue
            ds[i].insert(0, ds[i][0]-ds[i+1][0])
        print(ds)

        acc += ds[0][-1]
        acc2 += ds[0][0]
    print(acc)
    print(acc2)

if __name__ == '__main__':
    solve()
