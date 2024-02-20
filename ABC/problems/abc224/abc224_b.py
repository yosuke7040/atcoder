import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

isNo = False
for i1 in range(H-1):
    for i2 in range(i1, H):
        for j1 in range(W-1):
            for j2 in range(j1, W):
                if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                    isNo = True
                    break

if isNo:
    print("No")
else:
    print("Yes")
