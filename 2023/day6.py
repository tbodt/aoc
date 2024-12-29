import aoc
from collections import *
import re

inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def race_distance(total_time, held):
    return (total_time - held) * held

times, dists = inp.splitlines()
times = [int(x) for x in times.split()[1:]]
dists = [int(x) for x in dists.split()[1:]]

times2, dists2 = inp.splitlines()
time2 = int(''.join(times2.split()[1:]))
dist2 = int(''.join(dists2.split()[1:]))

def solve():
    acc=1
    for i in range(len(times)):
        ways = 0
        for t in range(0, times[i]+1):
            if race_distance(times[i], t) > dists[i]:
                ways += 1
        print(ways)
        acc *= ways
    print(acc)

    ways = 0
    for t in tqdm(range(0, time2+1)):
        if race_distance(time2, t) > dist2:
            ways += 1
    print(ways)

if __name__ == '__main__':
    solve()
