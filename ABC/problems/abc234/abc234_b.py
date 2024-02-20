import sys
sys.setrecursionlimit(10**6)
from itertools import product
import math

N = int(input())
xy = []
for i in range(N):
    xy.append(list(map(int, input().split())))

max_len = 0
for i in range(N-1):
    for j in range(i+1, N):
        x = abs(xy[i][0] - xy[j][0])
        if x == 0:
            x = 0.000001
        y = abs(xy[i][1] - xy[j][1])
        if y == 0:
            y = 0.000001
        length = math.sqrt(abs(x**2 + y**2))
        if max_len < length:
            max_len = length

print(max_len)