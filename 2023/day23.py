import aoc
import pprint
from collections import *
import re

inp = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#'''
inp = aoc.input(re.findall(r'day(\d+)', __file__)[-1])

DIRS = [(0,1),(1,0),(0,-1),(-1,0)]
R,D,L,U = DIRS
SLOPE = {'>':R,'<':L,'v':D,'^':U}

def addp(a, b):
    return tuple(a[i] + b[i] for i in range(len(a)))

g = {}
for r,rr in enumerate(inp.splitlines()):
    for c,cc in enumerate(rr):
        g[r,c] = cc

def adj(g, p):
    #if g[p] in SLOPE:
        #yield addp(p,SLOPE[g[p]])
        #return
    for d in DIRS:
        pp = addp(p,d)
        if pp not in g: continue
        if g[pp] == '#': continue
        yield pp
def adj_path(g, p):
    for a1 in adj(g, p):
        path = [p, a1]
        while True:
            nexts = list(a for a in adj(g,path[-1]) if a != path[-2])
            #print(path[-1], nexts)
            if len(nexts) == 1:
                path.append(nexts[0])
            else:
                yield len(path[1:-1]), path[-1]
                break

def solve():
    real_graph = {}
    q = deque()
    q.append((0,1))
    while q:
        p = q.popleft()
        if p in real_graph: continue
        thingz = list(adj_path(g,p))
        for path, a in thingz:
            q.append(a)
        real_graph[p] = thingz

    pprint.pprint(real_graph)
    #return

    for r in range(len(inp.splitlines())):
        print(r,end=' ')
        for c in range(len(inp.splitlines()[0])):
            print(g[r,c],end='')
        print()

    def longest_path_from(p, to, path_so_far=[]):
        path, aa = real_graph[p]
        if len(aa) == 0 and path[-1] == to: return path
        if set(path) & set(path_so_far):
            print('aa')
            return []
        path = [p] + path
        best_path = []
        #print(p, path, aa)
        for a in aa:
            #print(a, visited)
            if a in path:
                print('bb')
                continue
            rest_path = longest_path_from(a, to, path_so_far=path)
            if len(rest_path) > len(best_path):
                best_path = rest_path
        return path + best_path

    seen = defaultdict(int)
    cache = {}
    def longest_path_from(p, path_so_far=[]):
        #print(p, path_so_far)
        seen[p] += 1
        if len(path_so_far) < 7:
            print(len(path_so_far), p, seen[p])

        best = 0, path_so_far
        for w, aa in real_graph[p]:
            if any(pp == aa for _, pp in path_so_far):
                continue
            path = path_so_far + [(w, aa)]
            test = longest_path_from(aa, path)
            test = test[0]+w+1, test[1]
            if test > best:
                best = test
        return best

    w, path = longest_path_from((0,1))
    print(w, len(path), path)
    path = [x[1] for x in path]
    for r in range(len(inp.splitlines())):
        for c in range(len(inp.splitlines()[0])):
            if (r,c) in path:
                print('O',end='')
            else:
                print(g[r,c],end='')
        print()

if __name__ == '__main__':
    solve()
