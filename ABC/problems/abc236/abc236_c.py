import sys
sys.setrecursionlimit(10**6)
from itertools import product

N, M = map(int, input().split())
S = input().split(" ")
T = input().split(" ")

idx = 0

for i in range(N):
    if S[i] == T[idx]:
        print("Yes")
        idx += 1
    else:
        print("No")