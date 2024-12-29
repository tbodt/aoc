import aoc
from grid import addp
from collections import *
import re

inp='''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
'''
inp='''#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])
house, moves = inp.split('\n\n')
moves = moves.replace('\n','')

DIRS = {'^':(-1,0),'v':(1,0),'<':(0,-1),'>':(0,1)}

def dump(g):
    for r in range(max(r for r,c in g)+1):
        for c in range(max(c for r,c in g)+1):
            print(g.get((r,c),'.'),end='')
        print()

def solve():
    g = {}
    for r, l in enumerate(house.splitlines()):
        for c, ch in enumerate(l):
            if ch != '.':
                g[r,c] = ch
    robot = next(k for k, v in g.items() if v == '@')
    del g[robot]
    print(robot)
    for m in moves:
        dir = DIRS[m]
        print(dir)
        moved_robot = addp(robot, dir)
        p = moved_robot
        fail = False
        put_box = False
        while p in g:
            if g[p] == '#':
                fail = True
                break
            if g[p] == 'O':
                put_box = True
            p = addp(p, dir)
        if fail: continue
        if put_box:
            g[p] = 'O'
            del g[moved_robot]
        robot = moved_robot

        # g[robot] = '@'
        # dump(g)
        # del g[robot]

    acc = 0
    for p in g:
        if g[p] != 'O': continue
        acc += p[0] * 100 + p[1]
    print(acc)

def solve2():
    g = {}
    for r, l in enumerate(house.splitlines()):
        for c, ch in enumerate(l):
            if ch == '.': continue
            g[r,c*2] = {'O':'['}.get(ch,ch)
            if ch != '@': g[r,c*2+1] = {'O':']'}.get(ch,ch)

    dump(g)

    robot = next(k for k, v in g.items() if v == '@')
    del g[robot]
    print(robot)

    for m in moves:
        dir = DIRS[m]
        print(dir)
        moved_robot = addp(robot, dir)

        fail = False
        push_points = set()
        new_push_points = [moved_robot]
        #import ipdb;ipdb.set_trace()
        while new_push_points:
            a = new_push_points
            new_push_points = []
            for p in a:
                if p in push_points: continue
                if p not in g:
                    continue
                if g[p] == '#':
                    fail = True
                    break
                if g[p] == '[':
                    new_push_points.append(addp(p, dir))
                    new_push_points.append(addp(p, (0,1)))
                if g[p] == ']':
                    new_push_points.append(addp(p, dir))
                    new_push_points.append(addp(p, (0,-1)))
                push_points.add(p)
            if fail: break
        if fail: continue

        print(push_points)
        cache = {}
        push_points = sorted(push_points, key=lambda a: a[0]*dir[0] + a[1]*dir[1], reverse=True)
        for p in push_points:
            off = addp(p, dir)
            #cache.setdefault(off, g[off])
            g[off] = g[p]
            del g[p]

        robot = moved_robot

        # g[robot] = '@'
        # dump(g)
        # del g[robot]

    acc = 0
    for p in g:
        if g[p] != '[': continue
        acc += p[0] * 100 + p[1]
    print(acc)

if __name__ == '__main__':
    solve()
    solve2()
