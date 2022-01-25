import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

N = int(input())
A = [0]*N
B = [0]*N

for i in range(N):
    A[i], B[i] = map(int, input().split())

ans = 0
left = 0
right = range(N) - 1
while( 1 ):
    