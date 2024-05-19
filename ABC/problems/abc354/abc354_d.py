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
# 優先度付きキュー
# from heapq import heapify, heappush, heappop

# 解説を見て実装（振り返りDがわかりやすい）
# https://www.youtube.com/watch?v=AHn4XUIvtwg

A, B, C, D = map(int, input().split())
# マイナスを考えないようにするために平行移動させる
A += 10**9
B += 10**9
C += 10**9
D += 10**9


# (0,0) -> (4,2)が1つのフォーマットになっている
# 面積の2倍を回答としているから、8がベース
def solve(W, H):
    ret = 0
    ret += 8 * (H // 2) * (W // 4)

    if H % 2 != 0:
        ret += 4 * (W // 4)

    if W % 4 >= 1:
        ret += 3 * (H // 2)
    if W % 4 >= 2:
        ret += 3 * (H // 2)
    if W % 4 >= 3:
        ret += 1 * (H // 2)

    H %= 2
    W %= 4
    if H != 0:
        if W >= 1:
            ret += 2
        if W >= 2:
            ret += 1

    return ret


# print(solve(A, B))
# print(solve(A, D))
# print(solve(C, B))
# print(solve(C, D))
print(solve(A, B) - solve(A, D) - solve(C, B) + solve(C, D))
