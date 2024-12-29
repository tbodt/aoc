import aoc
from collections import *
import re

inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def solve():
    muls = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', inp)
    s = 0
    for (a, b) in muls:
        s += int(a)*int(b)
    print(s)
    muls = re.findall(r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))', inp)
    on = True
    s = 0
    for (all, a, b) in muls:
        print(all)
        if all == 'do()': on = True
        elif all == 'don\'t()': on = False
        elif on: s += int(a)*int(b)
    #print(muls)
    print(s)

if __name__ == '__main__':
    solve()
