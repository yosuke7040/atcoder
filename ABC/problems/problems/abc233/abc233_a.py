import sys
sys.setrecursionlimit(10**6)
from itertools import product

X, Y = map(int, input().split())

diff = Y - X
cnt = 0

if diff <= 0:
    print(0)
else:
    while diff > (10*cnt):
        cnt += 1
    
    print(cnt)