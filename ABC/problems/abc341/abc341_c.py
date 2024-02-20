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


H, W, N = map(int, input().split())
T = input()
S = list(input() for _ in range(H))

ans = 0
for i in range(1, H - 1):
    for j in range(1, W - 1):
        if S[i][j] == "#":
            continue

        pos = [i, j]
        valid = True
        for k in T:
            if k == "R":
                pos[1] += 1
            elif k == "L":
                pos[1] -= 1
            elif k == "U":
                pos[0] -= 1
            elif k == "D":
                pos[0] += 1

            if S[pos[0]][pos[1]] == "#":
                valid = False
                break

        if valid:
            ans += 1
print(ans)
