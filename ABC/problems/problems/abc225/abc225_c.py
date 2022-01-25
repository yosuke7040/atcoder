import sys
sys.setrecursionlimit(10**6)
from decimal import Decimal

N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

isValid = True
for i in range(N):
    for j in range(M):
        if j < M-1 and B[i][j] + 1 != B[i][j+1]:
            isValid = False
        if i < N-1 and B[i][j] + 7 != B[i+1][j]:
            isValid = False
        if B[i][j] % 7 == 0 and j != M-1:
            isValid = False

if isValid:
    print("Yes")
else:
    print('No')