import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

# N = int(input())
# S = list(map(int, input().split()))

# ans = set()
# a = 1
# b = 1

# cnt = 0
# init = False

# for i in range(N):
#     init = True
#     a = 1
#     b = 1

#     while True:
#         ans = 4*a*b + 3*a+ 3*b

#         if ans == S[i]:
#             # print(i)
#             cnt += 1
#             # print("itti")
#             # print(ans, i)
#             break
#         elif ans < S[i]:
#             b += 1
#             init = False
#         elif ans > S[i]:
#             if init:
#                 # print("over")
#                 # print(ans, i)
#                 break
#             init = True
#             a += 1
#             b = 1

# print(N-cnt)

def f(a, b):
    return 4*a*b + 3*a + 3*b

N = int(input())
S = list(map(int, input().split()))
T = set()

for a in range(1, 1001):
    for b in range(1, 1001):
        T.add(f(a,b))

ans = 0

for x in S:
    if x not in T:
        ans += 1

print(ans)
