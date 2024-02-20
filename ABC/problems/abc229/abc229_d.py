import sys
sys.setrecursionlimit(10**6)
from itertools import product

S = input()
K = int(input())

# dp = [[0] * len(S) for _ in range(len(S))]
# for i in range(len(S)):
#     if S[i] == "x":
#         dp[0][i] = 1
#     else:
#         dp[0][i] = 0

# max_len = 0
# k = K
# for i in range(len(S)):
#     if dp[0][i]

#     for j in range(i, len(S)):
        


from collections import deque
que = deque()
stock = K
len = 0
max_len = 0

for char in S:
    len += 1
    if char == '.':
        stock -= 1
        que.append(1)
    else:
        que.append(0)

    while stock < 0:
        rm = que.popleft()
        if rm == 1:
            stock += 1
        len -= 1
    
    max_len = max(max_len , len)

print(max_len)
