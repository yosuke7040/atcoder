import sys
sys.setrecursionlimit(10**6)
from itertools import product

H, W = map(int, input().split())
C = list(input() for _ in range(H))

dp = [[0]*(W+1) for _ in range(H+1)]


for i in range(H-1, -1, -1):
    for j in range(W-1, -1, -1):
        if C[i][j] == ".":
            dp[i][j] = max(dp[i+1][j], dp[i][j+1]) + 1
        
# これWA出てたのは、いけないところも加算してたから
# （スタート地点周りが壁で囲まれてて、マックス１にしかならないときに
# その先で2以上の計算ができてしまってそれを回答としてしまうだろう)
# それをifで考慮するか、今回のように逆地点からDPしていく

# for i in range(1, H+1):
#     for j in range(1, W+1):
#         if C[i-1][j-1] == ".":
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
        # else:
        #     if dp[i-1][j] == 0 and dp[i][j-1] == 0:
        #         break
        #     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        #     dp[i][j] = 0
print(dp[0][0])