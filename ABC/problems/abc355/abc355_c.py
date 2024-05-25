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

N, T = map(int, input().split())
A = list(map(int, input().split()))

hit_rows_cnt = [[] for _ in range(N)]
hit_columns_cnt = [[] for _ in range(N)]
miginaname_cnt = []
# miginaname_cnt = [[] for _ in range(N)]
hidarinaname_cnt = []
# hidarinaname_cnt = [[] for _ in range(N)]

# hit_rows_cnt = 0
# hit_columns_cnt = 0
# miginaname_cnt = 0
# hidarinaname_cnt = 0
cnt = 0
for turn in A:
    cnt += 1
    # print("--------------------")
    # print("turn", turn)
    row_idx = turn // N
    if turn % N == 0:
        row_idx -= 1

    column_idx = (turn % N) - 1
    if column_idx == -1:
        column_idx = N - 1

    # print("row_idx", row_idx)
    # print("column_idx", column_idx)

    hit_rows_cnt[row_idx].append(turn)
    hit_columns_cnt[column_idx].append(turn)

    if row_idx == column_idx:
        miginaname_cnt.append(turn)
    if row_idx + column_idx == N - 1:
        hidarinaname_cnt.append(turn)

    # print("hit_rows_cnt", hit_rows_cnt)
    # print("hit_columns_cnt", hit_columns_cnt)
    # print("miginaname_cnt", miginaname_cnt)
    # print("hidarinaname_cnt", hidarinaname_cnt)

    if len(hit_rows_cnt[row_idx]) == N:
        print(cnt)
        exit()
    if len(hit_columns_cnt[column_idx]) == N:
        print(cnt)
        exit()
    if len(miginaname_cnt) == N:
        print(cnt)
        exit()
    if len(hidarinaname_cnt) == N:
        print(cnt)
        exit()

print(-1)
