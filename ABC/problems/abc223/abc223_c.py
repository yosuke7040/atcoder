import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

N = int(input())
A = [0]*N
B = [0]*N

for i in range(N):
    A[i], B[i] = map(int, input().split())

print(A)