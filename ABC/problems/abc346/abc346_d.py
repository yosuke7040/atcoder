import sys

sys.setrecursionlimit(10**6)
INF = 1 << 60


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


# from collections import defaultdict,Counter
# tmp = defaultdict(int)

N = int(input())
S = input()
C = list(map(int, input().split()))

# # 文字列 S をビット表現に変換
# bit_S = int(S, 2)
# print(bit_S)

# min_cost = float("inf")

# # 0をベースにした2文字続く文字列パターンの算出
# for pattern in range(4):  # '00', '01', '10', '11'
#     # パターンの作成（Nビットの長さ）
#     bit_pattern = int("{:b}".format(pattern) * (N // 2), 2)

#     # 差分（異なるビット）の計算
#     diff = bit_S ^ bit_pattern

#     # 差分がある位置でのコストの計算
#     cost = sum(C[i] for i in range(N) if diff & (1 << i))

#     # 最小コストの更新
#     min_cost = min(min_cost, cost)

# print(min_cost)

dp = [[[INF] * 2 for _ in range(2)] for _ in range(N)]

# 1次元目はSの順番
# 2次元目は回答が0か1か
# 3次元目は同じ数が並んだときに1
if S[0] == "0":
    dp[0][0][0] = 0
    dp[0][1][0] = C[0]
else:
    dp[0][0][0] = C[0]
    dp[0][1][0] = 0

for i in range(1, N):
    if S[i] == "0":
        dp[i][0][0] = dp[i - 1][1][0]
        dp[i][0][1] = min(dp[i - 1][0][0], dp[i - 1][1][1])
        # 1に変える場合（＝コストがかかる）
        dp[i][1][0] = dp[i - 1][0][0] + C[i]
        dp[i][1][1] = min(dp[i - 1][0][1], dp[i - 1][1][0]) + C[i]
    else:
        dp[i][1][0] = dp[i - 1][0][0]
        dp[i][1][1] = min(dp[i - 1][1][0], dp[i - 1][0][1])
        # 0に変える場合（＝コストがかかる）
        dp[i][0][0] = dp[i - 1][1][0] + C[i]
        dp[i][0][1] = min(dp[i - 1][1][1], dp[i - 1][0][0]) + C[i]

ans = min(dp[N - 1][0][1], dp[N - 1][1][1])
print(ans)
