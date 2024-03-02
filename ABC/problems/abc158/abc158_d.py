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


from collections import deque

S_deque = deque()

S = input()
for s in S:
    S_deque.append(s)

Q = int(input())
Queries = [list(input().split()) for _ in range(Q)]

isReversed = False
for query in Queries:
    if query[0] == "1":
        isReversed = not isReversed
    else:
        if query[1] == "1":
            if isReversed:
                S_deque.append(query[2])
            else:
                S_deque.appendleft(query[2])
        else:
            if isReversed:
                S_deque.appendleft(query[2])
            else:
                S_deque.append(query[2])

print("".join(S_deque) if not isReversed else "".join(S_deque)[::-1])
