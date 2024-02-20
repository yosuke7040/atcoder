import itertools
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


# 順列
# (1,2,3),(1,3,2),(2,1,3),(2,3,1),...,(3,2,1)
# for seq initertools.permutations(range(1,4)):

# 重複なしの組み合わせ
# (1,2,3),(1,2,4),...,(7,8,9)
# for seq initertools.combinations(range(1,10),3):

# 重複ありの組み合わせ
# (1,1,1),(1,1,2),...,(9,9,9)
# for seq initertools.combinations_with_replacement(range(1,10),3):

# 直積
# (1,1),(1,2),(1,3),(2,1),(2,2),...,(3,3)
# for seq initertools.product(range(1,4),range(1,4)):


N, K = map(int, input().split())
time = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for root in itertools.permutations(range(1, N)):
    now_time = 0
    now_time += time[0][root[0]]
    now_city = root[0]

    for i in range(1, N - 1):
        to_city = root[i]
        now_time += time[now_city][to_city]
        now_city = to_city

    now_time += time[now_city][0]
    if now_time == K:
        ans += 1

print(ans)
