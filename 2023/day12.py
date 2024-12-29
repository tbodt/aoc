import aoc
import functools
from collections import *
import re

inp='''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def works(pat, so_far):
    for i, c in enumerate(so_far):
        if pat[i] == c or pat[i] == '?':
            continue
        return False
    return True

@functools.lru_cache
def nperms(pat, nums):
    #print(pat, nums)
    acc = 0
    if len(nums) == 0:
        rest = '.'*len(pat)
        return 1 if works(pat, rest) else 0
    # place first number everywhere possible
    num = nums[0]
    for offset in range(0, len(pat)-num+1):
        so_far = '.'*offset + '#'*num
        if len(so_far) < len(pat): so_far += '.'
        if not works(pat, so_far): continue
        n = nperms(pat[len(so_far):], nums[1:])
        acc += n
    return acc

def solve():
    acc = 0
    for a in inp.splitlines():
        pat, nums = a.split()
        nums = [int(x) for x in nums.split(',')]
        n = nperms(pat, tuple(nums))
        print(pat, nums, n)
        acc += n
    print(acc)

    acc = 0
    for a in inp.splitlines():
        pat, nums = a.split()
        nums = [int(x) for x in nums.split(',')]
        pat = '?'.join([pat] * 5)
        nums = nums * 5
        n = nperms(pat, tuple(nums))
        print(pat, nums, n)
        acc += n
    print(acc)

if __name__ == '__main__':
    solve()
