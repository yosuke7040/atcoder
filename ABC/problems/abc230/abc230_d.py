import sys
sys.setrecursionlimit(10**6)
from itertools import product

N, D = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(N)]

LR.sort(key=lambda x: x[1])

# cnt = 0
# i = 0
# while i < N:
#     cnt += 1
#     punch_range = LR[i][1]+D-1
#     print(punch_range, i)
#     while i < N:
#         i += 1
#         print(i)
#         if LR[i][0] > punch_range:
#             i -= 1
#             break

# print(cnt)

ans = 0
x = 0

for l, r in LR:
    if x < l:
        ans += 1
        x = r+D-1

print(ans)