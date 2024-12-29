import aoc
from collections import *
import re

inp='''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

mods = {}

class Mod(object):
    def __repr__(self): return 'Mod('+repr(vars(self))+')'

LOW=False
HIGH=True

for l in inp.splitlines():
    name, targets = l.split(' -> ')
    if name[0] in '%&':
        t = name[0]
        name = name[1:]
    else:
        t = None
    m = Mod()
    m.targets = targets.split(', ')
    m.name = name
    m.t = t
    mods[name] = m

inps = defaultdict(list)
for m in mods.values():
    for t in m.targets:
        inps[t].append(m.name)

def solve():
    state = {}
    for m in mods.values():
        if m.t == '%': state[m.name] = LOW
        elif m.t == '&': state[m.name] = {i:LOW for i in inps[m.name]}

    hubs = ['dt','gr','xm','vt']

    acc = [0,0]
    lasty = {}
    last_out = {}
    def press_button(i, state):
        pulses = deque()
        def cast(mod, pwr):
            for t in mod.targets:
                pulses.append((mod.name, t, pwr))
        pulses.append(('button', 'broadcaster', LOW))
        while pulses:
            src, mod, pwr = pulses.popleft()
            spwr = 'low' if pwr == LOW else 'high'
            acc[pwr] += 1
            if mod == 'rx' and pwr == LOW: print('aaa')
                #print(i, f'{src} -{spwr}-> {mod}')
            if mod not in mods: continue
            mod = mods[mod]
            if mod.name == 'broadcaster':
                cast(mod, LOW)
            elif mod.t == '%':
                if pwr == HIGH: continue
                flop = not state[mod.name]
                state[mod.name] = flop
                cast(mod, flop)
            elif mod.t == '&':
                state[mod.name][src] = pwr
                florp = not all(state[mod.name].values())
                if mod.name == 'rm' and pwr == HIGH:
                    print(i, src, mod.name)
                    if src in lasty:
                        last_out[src] = (i-lasty[src], i%(i-lasty[src]))
                        print('last', src, last_out, 'ago')
                        print(last_out)
                    lasty[src] = i
                #print(state[mod.name], florp)
                cast(mod, florp)
            else:
                raise

    i = 0
    while True:
        press_button(i, state)
        #d = {}
        #for h in hubs: d.update(state[h])
        #print(d)
        i += 1
        if i == 1000:
            print(acc)
            print(acc[0]*acc[1])

def dot():
    print('digraph {')
    for m in mods.values():
        mty = m.t or ''
        for t in m.targets:
            if t in mods:
                tty = mods[t].t or ''
            else:
                tty = ''
            print(f'"{mty}{m.name}" -> "{tty}{t}";')
    print('}')

if __name__ == '__main__':
    solve()
