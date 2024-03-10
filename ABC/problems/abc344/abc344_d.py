import sys

sys.setrecursionlimit(10**6)
INF = float("inf")


# 最大公約数
def gcd_e(a, b):
    while b:
        a, b = b, a % b
    return a


# 最小公倍数
def lcm_e(a, b):
    return a * b / gcd_e(a, b)


# 二次元平面上で3点が同一直線上にあるか判定
def are_points_collinear(x1, y1, x2, y2, x3, y3):
    # 分母がゼロになる可能性をチェック
    if (x2 - x1) == 0 and (x3 - x1) == 0:
        return True
    if (x2 - x1) == 0 or (x3 - x1) == 0:
        return False

    # # 傾きを計算して比較
    # slope1 = (y2 - y1) / (x2 - x1)
    # slope2 = (y3 - y1) / (x3 - x1)
    # 傾き計算にすると誤差が出ると思うから、分子分母を掛けて比較
    slope1 = (y2 - y1) * (x3 - x1)
    slope2 = (y3 - y1) * (x2 - x1)

    return slope1 == slope2


T = input()
N = int(input())
# A = list()
# S = list()
# for i in range(N):
#     tmp = input().split()
#     A.append(int(tmp[0]))
#     S.append(tmp[1:])
A = [input().split()[1:] for _ in range(N)]

dp = [[INF] * (len(T) + 1) for _ in range(len(A) + 1)]
dp[0][0] = 0

for i in range(1, len(A) + 1):
    for j in range(len(T) + 1):
        # 袋の中のどの文字も追加しない場合
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        for s in A[i - 1]:
            k = len(s)
            # s がTの一部と一致し、文字を追加すする場合
            if j + k <= len(T) and T[j : j + k] == s:
                dp[i][j + k] = min(dp[i][j + k], dp[i - 1][j] + 1)

ans = dp[len(A)][len(T)]
if ans == INF:
    ans = -1
print(ans)
