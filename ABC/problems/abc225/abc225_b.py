import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]
# edges = [[0]*2 for _ in range(n-1)]
# for i in range(n-1):
#     tmp = input()
#     _tmp = tmp.split()
#     for j in range(2):
#         edges[i][j] = int(_tmp[j])
edge1 = edges[0][0]
edge2 = edges[0][1]
ans = 0
if edge1 == edges[1][0]:
    ans = edges[1][0]
elif edge1 == edges[1][1]:
    ans = edges[1][1]
elif edge2 == edges[1][0]:
    ans = edges[1][0]
elif edge2 == edges[1][1]:
    ans = edges[1][1]


isStar = True
for i in range(1, n-1):
    if ans == edges[i][0] or ans == edges[i][1]:
        pass
    else:
        isStar = False

if isStar:
    print("Yes")
else:
    print("No")