import sys
sys.setrecursionlimit(10**6)
from itertools import product

alpha = 'abcdefghijklmnopqrstuvwxyz'

S = input()
T = input()

K = 0
idx_S = 0
idx_T = 0

# Kを求める
while alpha[idx_S] != S[0]:
    idx_S += 1

while alpha[idx_T] != T[0]:
    idx_T += 1

while idx_T != idx_S:
    idx_S += 1
    K += 1
    if idx_S == 26:
        idx_S = 0

for i in range(len(S)):
    
    idx = 0
    while alpha[idx] != S[i]:
        idx += 1

    idx += K
    if idx >= 26:
        idx -= 26
    if T[i] != alpha[idx]:
        print("No")
        exit()

print("Yes")

#     idx_S = 0
#     idx_T = 0
#     cnt = 0
#     while alpha[idx_S] != S[i]:
#         idx_S += 1

#     while alpha[idx_T] != T[i]:
#         idx_T += 1

#     while idx_T != idx_S:
#         idx_S += 1
#         cnt += 1
#         if idx_S == 16:
#             idx_S = 0

#     if K != cnt:
#         print("No")
#         exit()

# print('Yes')