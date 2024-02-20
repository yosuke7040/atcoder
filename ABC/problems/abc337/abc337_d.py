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


def min_operations_to_make_o(H, W, K, grid):
    muri = True

    count = 10**5
    # 横チェック
    for i in range(H):
        for j in range(W - K + 1):
            x = 0
            for k in range(K):
                if grid[i][j + k] == "x":
                    x += 1
            if x != 0:
                continue

            ten = 0
            for k in range(K):
                ten += grid[i][j + k] == "."
            muri = False
            if ten < count:
                count = ten
    # 縦チェック
    for i in range(H - K + 1):
        for j in range(W):
            x = 0
            for k in range(K):
                if grid[i + k][j] == "x":
                    x += 1
            if x != 0:
                continue

            ten = 0
            for k in range(K):
                ten += grid[i + k][j] == "."
            # print(f"i: {i}, j: {j}, K: {K}, ten: {ten}")
            muri = False
            if ten < count:
                count = ten

    if muri:
        return -1

    return count


H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]


print(min_operations_to_make_o(H, W, K, S))
