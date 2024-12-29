import aoc
from collections import *
import re

inp='''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

class Range:
    def __init__(self, start, length):
        self.start = start
        self.length = length

class RangeMap:
    def __init__(self):
        self.ranges = []
    def add_range(self,dst, src, leng):
        self.ranges.append((src, dst, leng))
        self.ranges.sort()
    def lookup(self,src):
        for i, r in enumerate(self.ranges):
            if src >= r[0] and src <= r[0]+r[2]:
                #print(src, r)
                return src - r[0] + r[1]
        return src
    def __repr__(self):
        return repr(self.ranges)

maps = {}
seeds = inp.split('\n\n')[0].split(': ')[1]
seeds = list(map(int,seeds.split()))
for a in inp.split('\n\n')[1:]:
    a=a.splitlines()
    key, _, value = a[0].split()[0].split('-')
    m = RangeMap()
    for line in a[1:]:
        dst_start, src_start, length = map(int,line.split())
        m.add_range(dst_start, src_start, length)
    maps[key] = (value, m)

def solve():
    print(maps['seed'])

    path = ['seed','soil','fertilizer','water','light','temperature','humidity','location']

    minloc = float('inf')
    for seed in seeds:
        a = seed
        for i in range(len(path)-1):
            a = maps[path[i]][1].lookup(a)
        if a < minloc: minloc = a
    print(minloc)

    def best_in_range(start, leng, t='seed'):
        dent=('  '*(path.index(t)))[:-1]
        print(dent,t, start, leng)
        if t == 'location':
            return start
        t, m = maps[t]
        minloc = float('inf')
        last_end = start
        for r_src,r_dst,r_leng in m.ranges:
            # if start,leng intersects r_src,r_leng
            is_start = max(start,r_src)
            is_leng = min(start+leng,r_src+r_leng) - is_start
            if is_leng > 0:
                print(dent, r_src,r_dst,r_leng)
                minloc = min(minloc, best_in_range(is_start - r_src + r_dst, is_leng, t))
            # try before?
            b_start = max(last_end, start)
            b_end = min(r_src, start+leng)
            b_leng = b_end - b_start
            if b_leng > 0:
                print(dent, 'b', b_start, b_leng, ' ', last_end, r_src, start+leng)
                minloc = min(minloc, best_in_range(b_start, b_leng, t))
            last_end = r_src+r_leng
        # and try after
        a_start = max(last_end, start)
        a_leng = start+leng - a_start
        if a_leng > 0:
            print(dent,'a', a_start, a_leng)
            minloc = min(minloc, best_in_range(a_start, a_leng, t))
        return minloc

    minloc = float('inf')
    for i in range(0, len(seeds), 2):
        a = best_in_range(seeds[i],seeds[i+1])
        if a < minloc: minloc = a
        print()
    print(minloc)

if __name__ == '__main__':
    solve()
