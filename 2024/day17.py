from collections import *
import z3
import pprint
import re

inp=''''''
regs = [66752888, 0, 0]
prog = [2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0]

def seq(a):
    s = []
    while a:
        s.append(a%8)
        a //= 8
    return s

def my_prog(a):
    o = []
    print(oct(a))
    while a:
        b = a & 7
        bit = b ^ 7
        print(b, bit, (a >> bit) & 7)
        b ^= (a >> bit) & 7
        a >>= 3
        o.append(b)
    return o

def my_prog2(a):
    o = []
    print(oct(a))
    for i in range(10):
        octit = (a >> (i*3)) & 7
        octit ^= (a >> (i*3 + (octit ^ 7))) & 7
        o.append(octit)
    return o

def myprog_z3(target):
    s = z3.Optimize()
    a = z3.BitVec('a', 64)
    for i in range(len(target)):
        octit = (a >> (i*3)) & 7
        octit ^= (a >> (i*3 + (octit ^ 7))) & 7
        s.add(z3.simplify(octit) == target[i])
    s.minimize(a)
    # ken = []
    # while s.check() == z3.sat:
    #     k = s.model()[a]
    #     ken.append(k)
    #     s.add(a != k)
    #return min([k.as_long() for k in ken])
    return s

# 2 4 bst. b = a % 8
# 1 7 bxl. b ^= 7
# 7 5 cdv. c = a / 2**b
# 1 7 bxl. b ^= 7
# 0 3 adv. a = a / 2**3
# 4 1 bxc. b ^= c
# 5 5 out. out b % 8
# 3 0 jnz. if a != 0 loop

def solve():
    ip = 0
    a, b, c = regs
    def combo(n):
        if 0 <= n <= 3: return n
        elif n == 4: return a
        elif n == 5: return b
        elif n == 6: return c
        elif n == 7: raise
    o = []

    while ip < len(prog):
        #print(ip, end=' ')
        inst = prog[ip]
        arg = prog[ip+1]
        #print(inst, arg, end=' ')
        ip += 2
        if inst == 0:
            #print('adv')
            a = a//(2**combo(arg))
        elif inst == 1:
            #print('bxl')
            b ^= arg
        elif inst == 2:
            #print('bst')
            b = combo(arg) % 8
        elif inst == 3:
            #print('jnz')
            if a != 0: ip = arg
        elif inst == 4:
            #print('bxc')
            b ^= c
        elif inst == 5:
            oa = combo(arg)%8
            #print('out', oa)
            o.append(oa)
        elif inst == 6:
            #print('bdv')
            b = a//(2**combo(arg))
        elif inst == 7:
            #print('cdv')
            c = a//(2**combo(arg))
        else:
            print(inst)
            raise

    #print(prog)
    print(o)
    #print(','.join(map(str,o)))

    print(my_prog(regs[0]))

if __name__ == '__main__':
    solve()
