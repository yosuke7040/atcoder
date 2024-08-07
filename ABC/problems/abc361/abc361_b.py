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

# 優先度付きキュー
# from heapq import heapify, heappush, heappop

# ソート状態で要素の追加・削除が可能なリスト。
# from sortedcontainers import SortedSet, SortedList, SortedDict

a,b,c,d,e,f = map(int,input().split())
g,h,i,j,k,l = map(int,input().split())


# if not (a < g < d):
#     print("No")
#     exit()
# if not (b < h < e):
#     print("No")
#     exit()

# if not (c < i < f):
#     print("No")
#     exit()

# print("Yes")

overlap_x = max(0, min(d, j) - max(a, g))
overlap_y = max(0, min(e, k) - max(b, h))
overlap_z = max(0, min(f, l) - max(c, i))

if overlap_x > 0 and overlap_y > 0 and overlap_z > 0:
    print("Yes")
else:
    print("No")
