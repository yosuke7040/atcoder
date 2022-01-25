import sys
sys.setrecursionlimit(10**6)
from itertools import product

N = int(input())
H = list(map(int, input().split()))

ans = H[0]
for i in range(1, N):
    # print(ans, H[i])
    if ans < H[i]:
        ans = H[i]
    else:
        break

print(ans)