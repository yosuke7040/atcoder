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

if S[0] != "A":
    print("WA")
    exit()

if not S[1].islower():
    print("WA")
    exit()

if S[2:-1].count("C") != 1:
    print("WA")
    exit()

if not S[-1].islower():
    print("WA")
    exit()

if not S.replace("C", "").replace("A", "").islower():
    # NOTE：これは4文字の時、空の文字列を返している
    # print(S[2:-1].replace("C", "").islower())
    # 小文字が含まれていないから、そもそもislower()でFalseになる
    # if not S[2:-1].replace("C", "").islower():
    print("WA")
    exit()


print("AC")
