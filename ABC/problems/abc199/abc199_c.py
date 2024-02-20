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
S = input()
S_array = list(S)
Q = int(input())
TAB = [list(map(int, input().split())) for _ in range(Q)]
irekae = False

for i in range(Q):
    if TAB[i][0] == 1:
        if irekae:
            tmp_a = (TAB[i][1] + N) % (2 * N)
            tmp_b = (TAB[i][2] + N) % (2 * N)
            S_array[tmp_a - 1], S_array[tmp_b - 1] = (
                S_array[tmp_b - 1],
                S_array[tmp_a - 1],
            )
        else:
            S_array[TAB[i][1] - 1], S_array[TAB[i][2] - 1] = (
                S_array[TAB[i][2] - 1],
                S_array[TAB[i][1] - 1],
            )
    else:
        # ↓N回の処理が走る
        # S_array = S_array[N:] + S_array[:N]
        # 実際には入れ替えない
        irekae = not irekae

if irekae:
    S_array = S_array[N:] + S_array[:N]
    print("".join(map(str, S_array)))
else:
    print("".join(map(str, S_array)))
