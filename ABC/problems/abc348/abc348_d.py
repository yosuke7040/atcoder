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

H, W = map(int, input().split())
A = [input() for _ in range(H)]
N = int(input())
R = [list(map(int, input().split())) for _ in range(N)]


from collections import deque


def can_reach_goal_fixed(h, w, grid, n, medicines):
    # マスの状態をマッピング
    empty, obstacle, start, goal = ".", "#", "S", "T"

    # スタートとゴールの位置を見つける
    start_pos, goal_pos = None, None
    for i in range(h):
        for j in range(w):
            if grid[i][j] == start:
                start_pos = (i, j)
            elif grid[i][j] == goal:
                goal_pos = (i, j)

    # 薬の位置とエネルギーを辞書で管理
    medicine_dict = {(r - 1, c - 1): e for r, c, e in medicines}

    # BFSを実行
    visited = set()  # (i, j)をキーとして使用
    queue = deque([(start_pos[0], start_pos[1], 0)])  # (i, j, energy)
    while queue:
        i, j, energy = queue.popleft()

        # ゴールに到達したかチェック
        if (i, j) == goal_pos:
            return "Yes"

        # 既に訪問済みかチェック
        if (i, j) in visited and energy <= 0:
            continue
        visited.add((i, j))

        # 現在地に薬があればエネルギーを更新
        if (i, j) in medicine_dict:
            energy = max(energy, medicine_dict[(i, j)])

        # 隣接する空きマスを探索
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] != obstacle and energy > 0:
                queue.append((ni, nj, energy - 1))

    return "No"


can_reach_goal_fixed(H, W, A, N, R)
