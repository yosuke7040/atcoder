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

# S = "wbwbwwbwbwbw"
S = "wbwbwwbwbwbw" * 17
W, B = map(int, input().split())

for i in range(12):
    tmp_S = S[i:]
    tmp_W = W
    tmp_B = B
    is_ok = True

    for j in range(W + B):
        # print(f"j={j}")
        if tmp_S[j] == "w":
            tmp_W -= 1
        else:
            tmp_B -= 1

        if tmp_W < 0 or tmp_B < 0:
            # print(tmp_W, tmp_B)
            # print("----")
            is_ok = False
            break

    if is_ok:
        print("Yes")
        exit()

print("No")
