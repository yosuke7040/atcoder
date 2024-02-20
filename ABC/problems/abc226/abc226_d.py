import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

s = set()

N = int(input())
loc = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        X = loc[i][0] - loc[j][0]
        Y = loc[i][1] - loc[j][1]
        g = gcd(abs(X), abs(Y))
        s.add((X//g, Y//g))

print(len(s))
