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


N, T = map(int, input().split())
A = []
B = []
for i in range(T):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A_score = dict()
for i in range(N):
    A_score[i + 1] = 0

A_count = dict()
A_count[0] = N
# A_score = [0 for _ in range(N)]

ans = set()
ans.add(0)
for i in range(T):
    A_count[A_score[A[i]]] -= 1
    if A_count[A_score[A[i]]] == 0:
        # print(A_score, A[i])
        ans.remove(A_score[A[i]])

    A_score[A[i]] += B[i]
    ans.add(A_score[A[i]])
    if A_score[A[i]] in A_count:
        A_count[A_score[A[i]]] += 1
    else:
        A_count[A_score[A[i]]] = 1

    # print(A_score)
    # print(A_count)
    # print(ans)
    print(len(ans))
    # print("----------")
