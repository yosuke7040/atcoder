import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

N, K, A = map(int, input().split())

idx = A
for i in range(K-1):
    idx += 1
    if idx == N+1:
        idx = 1

print(idx)