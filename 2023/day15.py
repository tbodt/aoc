import aoc
from collections import *
import re

inp='''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def hash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v

def solve():
    insts = inp.split(',')
    acc=0
    for i in insts:
        acc += hash(i)
    print(acc)

    boxes = [({},[]) for _ in range(256)]
    for i in insts:
        lab = re.findall(r'^[a-z]*', i)[0]
        h = hash(lab)
        d,a = boxes[h]
        if '-' in i:
            if lab in d:
                del d[lab]
                a.remove(lab)
        else:
            foc = int(i.split('=')[1])
            d[lab] = foc
            if lab not in a: a.append(lab)
        boxes[h] = d,a
    print(boxes)

    acc = 0
    for i_box, b in enumerate(boxes):
        for i_lens, lens in enumerate(b[1]):
            acc += (i_box+1)*(i_lens+1)*b[0][lens]
    print(acc)

if __name__ == '__main__':
    solve()
