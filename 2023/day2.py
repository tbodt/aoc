import aoc
from collections import *
import re

inp = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def solve():
    bag = {'red':12,'green':13,'blue':14}
    tot = 0
    for a in inp.splitlines():
        game_id = int(a.split(':')[0].split()[1])
        possible = True
        for test in a.split(': ')[1].split(';'):
            for b in test.split(', '):
                count, color = b.split()
                count = int(count)
                if bag[color] < count: possible = False
        if possible:
            print(game_id)
            tot += game_id
    print('tot', tot)


    tot=0
    for a in inp.splitlines():
        poss = defaultdict(int)
        game_id = int(a.split(':')[0].split()[1])
        possible = True
        for test in a.split(': ')[1].split(';'):
            for b in test.split(', '):
                count, color = b.split()
                count = int(count)
                poss[color] = max(poss[color], count)
        print(game_id, poss)
        power=poss['red']*poss['blue']*poss['green']
        tot += power
        print(power)
    print('tot',tot)

if __name__ == '__main__':
    solve()
