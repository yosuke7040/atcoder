import sys
sys.setrecursionlimit(10**6)
from itertools import product

N, W = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(N)]
cheese = sorted(cheese, key=lambda x: x[0], reverse=True)

num_val = 0
for i in range(N):
    weight = cheese[i][0]
    if W - cheese[i][1] >= 0:
        num_val += (cheese[i][0] * cheese[i][1])
        W -= cheese[i][1]
    else:
        num_val += (cheese[i][0] * W)
        break

print(num_val)
