import sys
sys.setrecursionlimit(10**6)
from itertools import product

N, K = map(int, input().split())
P = [list(map(int,input().split())) for _ in range(N)]

points = [sum(row) for row in P]
sort_points = sorted(points, reverse=True)
target = sort_points[K-1]

for i in range(N):
    if points[i] + 300 >= target:
        print("Yes")
    else:
        print("No")