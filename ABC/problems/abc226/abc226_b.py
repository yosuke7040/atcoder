import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

# N = int(input())
# L = tuple(input() for _ in range(N))

# ans_list = {L[0]}
# cnt = 1

# for i in range(1, N):
#     if L[i] not in ans_list:
#         ans_list.add(L[i])
#         cnt += 1
# print(cnt)



# N = int(input())
# S = set(tuple(input() for _ in range(N)))
# print(len(S))


N = int(input())
S = set()

for _ in range(N):
    l, *A = map(int, input().split())
    A = tuple(A)
    S.add(A)

print(len(S))