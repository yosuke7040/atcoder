import sys

sys.setrecursionlimit(10**6)
INF = 1 << 60

# 大文字アルファベット
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 小文字アルファベット
lower_alpha = "abcdefghijklmnopqrstuvwxyz"

MOD = 998244353


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


# 素数判定
def isprime(N):
    if N < 2:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True


# from collections import defaultdict,Counter
# tmp = defaultdict(int)

# 両端キュー
# from collections import deque
5
# 優先度付きキュー
# from heapq import heapify, heappush, heappop

# ソート状態で要素の追加・削除が可能なリスト。O(logN)
# from sortedcontainers import SortedSet, SortedList, SortedDict

import itertools

N, M = map(int, input().split())
S = list(input() for _ in range(N))

ans = N + 1

for i in range(1, N + 1):
    for seq in itertools.combinations(range(N), i):
        popcorn = [False] * M
        for idx in seq:
            for j in range(M):
                if S[idx][j] == "o":
                    popcorn[j] = True
        if all(popcorn):
            if ans > len(seq):
                ans = len(seq)


print(ans)