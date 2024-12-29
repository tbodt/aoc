import aoc
from pprint import pprint
from collections import *
import re

inp='''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

def parse_hand(h):
    hh = []
    for c in h:
        if c.isdigit(): hh.append(int(c))
        else: hh.append({'A':14,'K':13,'Q':12,'J':11,'T':10}[c])
    return tuple(hh)

def parse_hand2(h):
    hh = []
    for c in h:
        if c.isdigit(): hh.append(int(c))
        else: hh.append({'A':14,'K':13,'Q':12,'J':0,'T':10}[c])
    return tuple(hh)

def strength(h):
    count = Counter(h)
    counts = (list(count.values()))
    counts.sort(reverse=True)
    #$print(counts)
    if counts == [5]: return 7
    if counts == [4,1]: return 6
    if counts == [3,2]: return 5
    if counts == [3,1,1]: return 4
    if counts == [2,2,1]: return 3
    if counts == [2,1,1,1]: return 2
    return 1

def strength2(h):
    count = Counter(h)
    #print(h)
    if 0 in h and count[0] != 5:
        nzero = count[0]
        del count[0]
        print(h, count)
        mx = max(count.values())
        for k, v in count.items():
            if v == mx:
                break
        else:
            print(h)
            raise
        #print(count)
        count[k] += nzero
        #print(count)
    counts = (list(count.values()))
    counts.sort(reverse=True)
    #print(counts)


    print(counts)
    if counts == [5]: return 7
    if counts == [4,1]: return 6
    if counts == [3,2]: return 5
    if counts == [3,1,1]: return 4
    if counts == [2,2,1]: return 3
    if counts == [2,1,1,1]: return 2
    if counts == [1,1,1,1,1]: return 1
    raise

def solve():
    stuff = []
    for a in inp.splitlines():
        hand, bid = a.split()
        bid=int(bid)
        hand=parse_hand(hand)
        stuff.append((hand, bid))
    stuff.sort(key=lambda k: (strength(k[0]), k[0]))
    #pprint(stuff)
    acc=0
    for i, (hand, bid) in enumerate(stuff):
        rank=i+1
        count = Counter(hand)
        counts = (list(count.values()))
        counts.sort(reverse=True)
        #print(rank, hand, bid, strength(hand), counts)
        acc += rank*bid
    print(acc)

    stuff = []
    for a in inp.splitlines():
        hand, bid = a.split()
        bid=int(bid)
        hand=parse_hand2(hand)
        stuff.append((hand, bid))
    stuff.sort(key=lambda k: (strength2(k[0]), k[0]))
    #pprint(stuff)
    acc=0
    for i, (hand, bid) in enumerate(stuff):
        rank=i+1
        count = Counter(hand)
        counts = (list(count.values()))
        counts.sort(reverse=True)
        print(rank, hand, bid, strength2(hand),counts)
        acc += rank*bid
    print(acc)


if __name__ == '__main__':
    solve()
