import aoc
import pprint
import sortedcontainers
from collections import *
import re

inp='''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def brick_top(b):
    return max(b[0][2], b[1][2])

def brick_bottom(b):
    return min(b[0][2], b[1][2])

def brick_set_bottom(b, new_bottom):
    bottom_delta = new_bottom - brick_bottom(b)
    ((x1,y1,z1),(x2,y2,z2)) = b
    aa = ((x1,y1,z1 + bottom_delta),(x2,y2,z2 + bottom_delta))
    assert brick_bottom(aa) == new_bottom
    return aa

def brick_contains(b, p):
    return all(b[i] <= p[i] <= p[i] for i in range(3))

def range_intersects(r1, r2):
    return max(r1[0], r2[0]) <= min(r1[1], r2[1])

def brick_intersects(b1, b2):
    return all(range_intersects((b1[0][i], b1[1][i]), (b2[0][i], b2[1][i])) for i in range(3))

def fall(bricks, brick, ignoring=None):
    orig_brick = brick
    for i in reversed(range(bricks.bisect_left(brick))):
        if bricks[i] == ignoring:
            continue
        bottom = brick_top(bricks[i]) + 1
        test_brick = brick_set_bottom(brick, bottom - 1)
        #print('orig', orig_brick, 'moved to', test_brick, bottom, 'test intersects', bricks[i])
        if brick_intersects(test_brick, bricks[i]):
            break
    else:
        bottom = 1
    assert bottom <= brick_bottom(orig_brick)
    return brick_set_bottom(brick, bottom)

def is_supporting(bricks, brick):
    for i in range(bricks.bisect_right(brick), len(bricks)):
        brick_above = bricks[i]
        fallen = fall(bricks, brick_above, ignoring=brick)
        if brick_bottom(fallen) < brick_bottom(brick_above):
            return True
    return False

def all_supported(bricks, brick):
    l = []
    check_at_level = brick_top(brick) + 1
    for i in range(bricks.bisect_right(brick), len(bricks)):
        brick_above = bricks[i]
        if brick_bottom(brick_above) != check_at_level:
            continue
        test_brick = brick_set_bottom(brick_above, brick_bottom(brick_above) - 1)
        if brick_intersects(test_brick, brick):
            l.append(brick_above)
    return l

def solve():
    bricks = sortedcontainers.SortedList(key=brick_top)
    for l in inp.splitlines():
        bricks.add(tuple(map(lambda a: tuple(map(int, a.split(','))), l.split('~'))))

    for brick in list(bricks):
        fallen = fall(bricks, brick)

        print(brick, '->', fallen)
        bricks.remove(brick)
        bricks.add(fallen)

    above_dict = {b: set() for b in bricks}
    below_dict = {b: set() for b in bricks}
    for brick in list(bricks):
        supported_list = all_supported(bricks, brick)
        if len(supported_list):
            above_dict[brick] = set(supported_list)
        for supports in supported_list:
            below_dict[supports].add(brick)

    not_load_bearing = 0
    total_chains = 0
    for brick in bricks:
        # if removed, what would fall?
        fallen = set()
        falling = {brick}
        while falling:
            falling_next = set()
            for falling_brick in falling:
                bricks_above = above_dict[falling_brick]
                for b_above in bricks_above:
                    if len(below_dict[b_above] - fallen - falling) == 0:
                        falling_next.add(b_above)
            fallen.update(falling)
            falling = falling_next
        chained = len(fallen) - 1
        print(brick, fallen, chained, is_supporting(bricks, brick))
        if chained == 0:
            assert not is_supporting(bricks, brick)
            not_load_bearing += 1
        total_chains += chained

    print(not_load_bearing, total_chains)

if __name__ == '__main__':
    solve()
