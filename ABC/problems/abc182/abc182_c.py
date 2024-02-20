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


def min_digits_to_remove_for_multiple_of_three(n):
    list_n = list(str(n))
    amari_1 = False
    amari_2 = False

    for i in range(len(list_n)):
        if int(list_n[i]) % 3 == 1:
            amari_1 = True
        if int(list_n[i]) % 3 == 2:
            amari_2 = True

    if n % 3 == 0:
        return 0

    # 全体の余りが1
    if n % 3 == 1:
        # 余りが1の桁がある
        if amari_1:
            # 桁が1つの場合むり
            if len(list_n) == 1:
                return -1
            return 1

        # 余りが2の桁が2つある
        if amari_2:
            # 桁が2つの場合むり
            if len(list_n) == 2:
                return -1
            return 2

    # 全体の余りが2
    if n % 3 == 2:
        # 余りが2の桁がある
        if amari_2:
            # 桁が1つの場合むり
            if len(list_n) == 1:
                return -1
            return 1

        # 余りが1の桁が2つある
        if amari_1:
            # 桁が2つの場合むり
            if len(list_n) == 2:
                return -1
            return 2

    return -1


N = int(input())

print(min_digits_to_remove_for_multiple_of_three(N))
