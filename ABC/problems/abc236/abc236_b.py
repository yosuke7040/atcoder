import sys
sys.setrecursionlimit(10**6)
from itertools import product
from  collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
# print(c)
# print(c.keys())

cnt = 1
# for key in c:
#     print(key)
#     # print(c[i].values())
#     print(c[key])
#     if c[key] != 4:
#         # print(cnt)
#         break
#     cnt += 1

for i in range(1, N+1):
    # print(c[i])
    if c[i] != 4:
        print(i)
