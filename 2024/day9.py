import aoc
import array
from collections import *
import re

inp='''2333133121414131402'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

Block = namedtuple('Block', ['length', 'file'])

def solve():
    disk = []
    id = 0
    gap = False
    free = []
    for c in inp:
        n = int(c)
        if gap:
            place = None
        else:
            place = id
            id += 1
        for _ in range(n):
            disk.append(place)
            if place is None: free.append(len(disk)-1)
        gap = not gap

    disk = list(disk)
    free = free[::-1]
    while free:
        space = free.pop()
        if space >= len(disk): break
        move = disk.pop()
        while not move:
            move = disk.pop()
        assert disk[space] is None
        disk[space] = move
    print(sum(i * id for i,id in enumerate(disk)))

    blocks = []
    id = 0
    gap = False
    for c in inp:
        n = int(c)
        if gap:
            blocks.append(Block(n, None))
        else:
            blocks.append(Block(n, id))
            id += 1
        gap = not gap

    print(blocks)
    offsets = []
    while blocks:
        while blocks[-1].file is None: blocks.pop()
        move = blocks.pop()
        for i, block in enumerate(blocks):
            if block.file is not None: continue
            if move.length > block.length: continue
            blocks[i] = block._replace(length=block.length - move.length)
            blocks.insert(i, move)
            break
        else:
            # could not move file. record its offset instead.
            offset = sum(b.length for b in blocks)
            offsets.append((offset, move))
        #print(move, blocks, offsets)
        print(len(blocks),len(offsets))
    print(sum(sum(i*block.file for i in range(offset, offset+block.length)) for offset, block in offsets))


if __name__ == '__main__':
    solve()
