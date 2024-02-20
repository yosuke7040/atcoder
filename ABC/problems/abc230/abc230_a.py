import sys
sys.setrecursionlimit(10**6)
from itertools import product

S = input()
N = int(S)

if N >= 42:
    n = N + 1
    print('AGC' + str(n).zfill(3))
else:
    print('AGC' + S.zfill(3))