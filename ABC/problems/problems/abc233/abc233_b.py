import sys
sys.setrecursionlimit(10**6)
from itertools import product


L, R = map(int, input().split())
S = input()
# print(L, R)
revers_S = S[::-1]
start_id = len(S) - R

for i in range(len(S)):
    if i < L-1:
        print(S[i], end='')
    elif i > R-1:
        print(S[i], end='')
    else:
        print(revers_S[start_id], end='')
        start_id += 1
print('')