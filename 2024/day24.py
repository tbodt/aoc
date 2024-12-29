import aoc
import z3
from collections import *
import re

inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])
xy, w1 = inp.split('\n\n')
gates = []
for w in w1.splitlines():
    a, outp = w.split(' -> ')
    in1, op, in2 = a.split()
    gates.append((in1,op,in2,outp))
vars = set(a for (in1, op, in2, outp) in gates for a in [in1, in2, outp])
vars = {v: z3.BitVec(v, 1) for v in vars}
inputs = []
for l in xy.splitlines():
    v, n = l.split(': ')
    inputs.append((v,n))

def solve():
    s = z3.Solver()
    for in1, op, in2, outp in gates:
        if op == 'AND': expr = vars[in1] & vars[in2]
        elif op == 'OR': expr = vars[in1] | vars[in2]
        elif op == 'XOR': expr = vars[in1] ^ vars[in2]
        s.add(expr == vars[outp])
    for v, n in inputs:
        s.add(vars[v] == n)
    print(s.check())
    print(s.model())
    m = s.model()
    outputs = {name: m[var] for name, var in vars.items() if name.startswith('z')}
    print(outputs)
    intstr = ''.join(str(a[1]) for a in (sorted(outputs.items(), key=lambda a:a[0], reverse=True)))
    print(int(intstr,2))

swaps = [('z21', 'gmq'), ('frn', 'z05'), ('wnf', 'vtj'), ('wtt', 'z39')]
swaps = {a1: a2 for a, b in swaps for a1, a2 in [(a, b), (b, a)]}

def dot():
    print('digraph {')
    for in1, op, in2, outp in gates:
        outp = swaps.get(outp, outp)
        #print(f'{outp} [label="{outp}\\n({op})"];');
        print(f'{in1} -> {outp}; {in2} -> {outp};')
    print('}')

gates_by_input = {}
for (in1, op, in2, outp) in gates:
    outp = swaps.get(outp,outp)
    inputs = tuple(sorted([in1,in2]))
    key = inputs,op
    assert key not in gates_by_input
    gates_by_input[key] = outp

def assert_gate(in1, in2, op):
    inputs = tuple(sorted([in1,in2]))
    key = inputs,op
    out = gates_by_input[key]
    print(in1, op, in2, '->', out)
    return out

def assert_half_adder(in1, in2):
    # in1 ^ in2 -> out
    # in1 & in2 -> carry
    out = assert_gate(in1, in2, 'XOR')
    carry = assert_gate(in1, in2, 'AND')
    return carry, out

def assert_full_adder(in1, in2, carryin):
    carry1, inner = assert_half_adder(in1, in2)
    carry2, out = assert_half_adder(inner, carryin)
    carryout = assert_gate(carry1, carry2, 'OR')
    return out, carryout
    # carry1 | carry2 -> carryout

def solve2():
    carry, out = assert_half_adder('x00', 'y00')
    assert out == 'z00'
    for i in range(1, 45):
        out, carry = assert_full_adder(f'x{i:02}', f'y{i:02}', carry)
        assert out == f'z{i:02}'
    assert carry == f'z{i+1:02}'
    print(','.join(sorted(swaps)))

if __name__ == '__main__':
    solve()
