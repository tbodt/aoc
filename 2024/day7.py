import re
from collections import *

inp='''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''
with open('input7.txt') as f:
    inp = f.read()

def check(a, nums):
    if len(nums) == 1:
        return nums[0] == a
    rest = nums[:-1]
    # try add
    b = a - nums[-1]
    if check(b, rest): return True
    # try mul
    if a % nums[-1] == 0:
        b = a // nums[-1]
        if check(b, rest): return True
    return False

def check2(a, nums):
    if len(nums) == 1:
        return nums[0] == a
    last = nums[-1]
    rest = nums[:-1]
    # try add
    b = a - last
    if check2(b, rest): return True
    # try mul
    if a % last == 0:
        b = a // last
        if check2(b, rest): return True
    # try concat
    if str(a).endswith(str(last)):
        b = str(a).removesuffix(str(last))
        if b != '' and b != '-':
            b = int(b)
            if check2(b, rest): return True
    return False

def solve():
    eqs = []
    for eq in inp.splitlines():
        answer, nums = eq.split(': ')
        answer = int(answer)
        nums=list(map(int,nums.split()))
        eqs.append((answer,nums))

    if 0:
        s =0
        for a, nums in eqs:
            print(a, nums, check(a,nums))
            if check(a,nums): s+=a
        print(s)

    s =0
    for a, nums in eqs:
        print(a, nums, check2(a,nums))
        if check2(a,nums): s+=a
    print(s)

if __name__ == '__main__':
    solve()
