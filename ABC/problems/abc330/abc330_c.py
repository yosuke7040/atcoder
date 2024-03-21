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

import math

D = int(input())

min_diff = D
max_x = int(math.sqrt(D)) + 1

for x in range(max_x + 1):
    y_squared = D - x**2
    if y_squared < 0:
        continue
    y = int(math.sqrt(y_squared))
    diff = abs(x**2 + y**2 - D)
    min_diff = min(min_diff, diff)

    if y_squared != y**2:
        diff = abs(x**2 + (y + 1)**2 - D)
        min_diff = min(min_diff, diff)

print(min_diff)

# print('---------')
# print(math.sqrt(10))
# print(int(math.sqrt(10)))
