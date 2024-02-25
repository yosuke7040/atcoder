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


N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]

C = []
A = []
for i in range(N):
    C.append(CA[i][0])
    A.append(CA[i][1:])

ans = 10**10
for bit in range(1 << N):
    cost = 0
    skill = [0] * M

    for i in range(N):
        if bit & (1 << i):
            cost += C[i]
            for j in range(M):
                skill[j] += A[i][j]

    if min(skill) >= X:
        ans = min(cost, ans)

if ans == 10**10:
    print(-1)
else:
    print(ans)
