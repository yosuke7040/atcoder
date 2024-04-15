import sys

sys.setrecursionlimit(10**6)
INF = 1 << 60

# # 連結リストの各ノード
# class Node:
#     def __init__(self, value=""):
#         self.nex = None  # 次がどのノードを指すか
#         self.value = value  # ノードに付随している値

# # 連結リストの初期化
# nil = Node()
# nil.nex = nil

# # 連結リストへ先頭への要素の挿入
# def insert(v):
#     v.nex = nil.nex  # v の次を、現在の先頭に
#     nil.nex = v  # 先頭を v に書き換える

# # 先頭の要素を削除
# def erase():
#     if nil.nex == nil:
#         print("Error")
#     else:
#         nil.nex = nil.nex.nex
#         pass


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
# 両端キュー
# from collections import deque

N = int(input())
a = list(map(int, input().split()))

ans = [0] * 9
for i in range(N):
    if a[i] < 400:
        ans[0] = 1
    elif a[i] < 800:
        ans[1] = 1
    elif a[i] < 1200:
        ans[2] = 1
    elif a[i] < 1600:
        ans[3] = 1
    elif a[i] < 2000:
        ans[4] = 1
    elif a[i] < 2400:
        ans[5] = 1
    elif a[i] < 2800:
        ans[6] = 1
    elif a[i] < 3200:
        ans[7] = 1
    else:
        ans[8] += 1

minumum = 0
for i in range(8):
    if ans[i] > 0:
        minumum += 1

maxmum = minumum + ans[8] if minumum + ans[8] <= 8 else 8

print(minumum, maxmum)