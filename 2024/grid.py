def addp(a, b):
    return tuple(a[i] + b[i] for i in range(len(a)))

def gheight(g):
    return max(c for r,c in g)+1

def gwidth(g):
    return max(c for r,c in g)+1

# def dump(g):
#     for r in range(max(r for r,c in g)+1):
#         for c in range(max(c for r,c in g)+1):
#             print(g.get((r,c),'.'),end='')
#         print()

