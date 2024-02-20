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


S = input()

if 8 != len(S):
    print("No")
    exit()

# if S[0].islower():
#     print("No")
#     exit()
# if S[len(S) - 1].islower():
#     print("No")
#     exit()

# 最初と最後が数値化チェック
if not (S[0].isalpha() and S[len(S) - 1].isalpha()):
    print("No")
    exit()

try:
    int(S[1 : len(S) - 1])
except ValueError:
    print("No")
    exit()

aida = int(S[1 : len(S) - 1])

if 100000 <= aida <= 999999:
    print("Yes")
    exit()
print("No")
