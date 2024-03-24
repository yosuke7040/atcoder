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

N, K = map(int, input().split())
A = list(map(int, input().split()))

total_sum = K * (K + 1) // 2

tmp_a = set()
for a in A:
    if a in tmp_a:
        continue
    if K >= a:
        tmp_a.add(a)

    # if K <= a:
    #     total_sum -= a

sum_tmp_a = sum(tmp_a)
print(total_sum - sum_tmp_a)
# print(tmp_a)
# print(total_sum, sum_tmp_a)

# ans = set(i for i in range(1, K + 1))
# set_A = set(A)

# # ansからset_Aを引いて、残ったものを出力
# print(sum(ans - set_A))
