import sys
sys.setrecursionlimit(10**6)
from decimal import Decimal

# N = int(input())
# info = [list(map(int, input().split())) for _ in range(N)]

# _max_col = map(sum, zip(*info))
# max_col = next(_max_col) + 1
# dp = [[-1]*(max_col+1) for _ in range(N+1)]
# dp[1][info[0][0]] = 1

# for i in range(1, N):
#     for j in range(max_col+1):
#         if dp[i][j] > 0:
#             dp[i+1][j] = dp[i][j]

#             if j+info[i][0] <= max_col and dp[i+1][j+info[i][0]] == -1:
#                 dp[i+1][j+info[i][0]] = i+1

# for i in range(max_col+1):
#     if dp[N][i] == N:
#         print(i)
#         break
# print(dp)
# print(info)



N = int(input())
T = [0] * (N+1)
A = [0] * (N+1)
for i in range(1, N+1):
    T[i], K, *A[i] = map(int, input().split())

need = [False] * (N+1)
need[N] = True

for i in range(N, 1, -1):
    if need[i]:
        for child in A[i]:
            need[child] = True

print(sum(T[i] for i in range(1,N+1) if need[i]))

# print(A)