import sys
sys.setrecursionlimit(10**6)
from itertools import product
from collections import Counter, defaultdict

N, Q = map(int, input().split())
# a = list(map(int, input().split()))
# # xk = []
# for i in range(Q):
#     xk.append(list(map(int, input().split())))

# s = set(a)
# c = Counter(a)

# ans = {}
# for i in s:
#     mozi = str(i)
#     ans[mozi] = [0]

# for i in range(N):
#     # ans[str(a[i])].append(ans[str(a[i])][-1]+1)
#     ans[str(a[i])].append(i)

# for i in range(Q):
#     if xk[i][0] not in s:
#         print(-1)
#     else:
#         if xk[i][1] > c[xk[i][0]]:
#             print(-1)
#         else:
#             print(ans[str(xk[i][0])][xk[i][1]] + 1)

A = list(map(int, input().split()))
D = defaultdict(list)
for i, a in enumerate(A, 1):
    D[a].append(i)

for _ in range(Q):
    x, k = map(int, input().split())
    if k <= len(D[x]):
        print(D[x][k-1])
    else:
        print(-1)
