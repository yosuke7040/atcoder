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

# ソート状態で要素の追加・削除が可能なリスト。O(logN)
# from sortedcontainers import SortedSet, SortedList, SortedDict

N, M, K = map(int, input().split())
tests = []
for _ in range(M):
    *test_keys, result = input().split()
    Ci = int(test_keys[0])
    keys = list(map(int, test_keys[1:]))
    tests.append((Ci, keys, result))

total_combinations = 1 << N
valid_count = 0

for i in range(total_combinations):
    valid = True
    for test in tests:
        Ci, keys, result = test
        correct_keys_count = 0

        for key in keys:
            if (i & (1 << (key - 1))) != 0:
                correct_keys_count += 1

        if (result == "o" and correct_keys_count < K) or (
            result == "x" and correct_keys_count >= K
        ):
            valid = False
            break
    if valid:
        valid_count += 1

print(valid_count)
