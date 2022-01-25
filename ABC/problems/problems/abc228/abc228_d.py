import sys
sys.setrecursionlimit(10**6)
from itertools import product

# N = 2 ** 20
# A = [-1]*N
# mod_list = [0]
# Q = int(input())
# query = [list(map(int, input().split())) for _ in range(Q)]

# for i in range(Q):
#     if query[i][0] == 1:
#         h = query[i][1]
#         while 1:
#             if A[h % N] == -1:
#                 break
#             h += 1

#         A[h % N] = query[i][1]
#     else:
#         print(A[query[i][1] % N])

# https://www.youtube.com/watch?v=yQ9JDRbWzUk
n = 1 << 20
p = [-1] * (n+1)
A = [-1] * n

def root(x):
    if p[x] < 0:
        return x
    p[x] = root(p[x])
    return p[x]

def merge(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    if x < y:
        x, y = y, x
    p[x] += p[y]
    p[y] = x

q = int(input())

for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        h = x % n
        target = root(h)
        if target == n:
            target = root(0)
        A[target] = x
        merge(target, target + 1)
    
    if t == 2:
        print(A[x%n])