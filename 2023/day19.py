import aoc
from collections import *
import re

inp='''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

_workflows, _parts = inp.split('\n\n')
parts = []
for p in _parts.splitlines():
    part = {}
    part['x'],part['m'],part['a'],part['s']=map(int,re.findall('\d+',p))
    parts.append(part)


workflows = {}
for w in _workflows.splitlines():
    name = w.split('{')[0]
    steps = w.split('{')[1][:-1].split(',')
    workflows[name] = steps

def run(w, p):
    w = workflows[w]
    for s in w:
        if ':' in s:
            check, op = s.split(':')
            if '<' in check:
                comp = '<'
                l = lambda a,b: a<b
            elif '>' in check:
                comp = '>'
                l = lambda a,b: a>b
            var, num = check.split(comp)
            num=int(num)
            if not l(p[var], int(num)): continue
        else:
            op=s
        if op in 'AR': return op
        return run(op, p)

def ranges_size(r):
    acc = 1
    for start,stop in r.values(): acc *= stop-start
    return acc

def count(w, ranges=None):
    if ranges is None:
        ranges = {k: (1, 4001) for k in 'xmas'}
    else:
        ranges = dict(ranges)

    if w == 'A': return ranges_size(ranges)
    if w == 'R': return 0

    win=w
    w = workflows[w]
    acc = 0
    for s in w[:-1]:
        check, op = s.split(':')
        if '<' in check:
            comp = '<'
        elif '>' in check:
            comp = '>'
        var, num = check.split(comp)
        num=int(num)

        # ranges if condition is false
        # ranges2 if condition is true
        ranges2 = dict(ranges)
        start, stop = ranges[var]
        if comp == '<':
            # a >= b
            # a < b
            ranges[var] = num, stop
            ranges2[var] = start, num
        elif comp == '>':
            # a <= b
            # a > b
            ranges[var] = start, num+1
            ranges2[var] = num+1, stop
        x = count(op,ranges2)
        #print(win, op, ranges2, x)
        acc += count(op, ranges2)

    x = count(w[-1], ranges)
    #print(win, w[-1], ranges, x)
    acc += count(w[-1], ranges)
    #print('pini la', win, acc)
    return acc

def solve():
    acc = 0
    for part in parts:
        v = run('in',part)
        if v == 'A': acc += sum(part.values())
        print(part, v)
    print(acc)

    print(count('in'))

if __name__ == '__main__':
    solve()
