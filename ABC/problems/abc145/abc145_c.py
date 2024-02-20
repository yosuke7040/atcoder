import itertools
import math
import sys

sys.setrecursionlimit(10**6)


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


N = int(input())

XY = [list(map(int, input().split())) for _ in range(N)]

distanses = 0
for seq in itertools.permutations(range(N)):
    # print(seq)
    for i, v in enumerate(seq):
        # print(i, v)
        if i == len(seq) - 1:
            break

        x = (XY[v][0] - XY[seq[i + 1]][0]) ** 2
        y = (XY[v][1] - XY[seq[i + 1]][1]) ** 2
        # print("xとy:", x + y)
        distanses += math.sqrt(x + y)
        # print("distanses, x, y", distanses, x, y)

n = 1
for i in range(1, N + 1):
    n *= i
print(distanses / n)
