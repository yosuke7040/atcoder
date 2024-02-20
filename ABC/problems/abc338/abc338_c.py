import sys

import pulp

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


N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))


# # 線形計画の定義
# problem = pulp.LpProblem("atcoder", pulp.LpMaximize)


# x = pulp.LpVariable("x", 0, None, "Integer")
# y = pulp.LpVariable("y", 0, None, "Integer")

# # 目的関数の定義
# problem += x + y

# # 制約条件の定義
# problem += A[0] * x + B[0] * y <= Q[0]
# problem += A[1] * x + B[1] * y <= Q[1]

# # 解く
# status = problem.solve(pulp.PULP_CBC_CMD(msg=False))
# # print(pulp.LpStatus[status])

# # # 結果表示
# # print("Result")
# # print("x:", x.value())
# # print("y:", y.value())

# print(int(x.value() + y.value()))


# # 線形計画の定義
# problem = pulp.LpProblem("atcoder", pulp.LpMaximize)

# # 変数のリストを生成
# variables = pulp.LpVariable.dicts("Var", range(N), 0, None, pulp.LpInteger)

# # 目的関数の定義
# problem += pulp.lpSum(variables[i] for i in range(N))

# # 制約条件の定義
# for i in range(N):
#     problem += A[i] * variables[i] + B[i] * variables[i] <= Q[i]

# # 解く
# status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# # 結果表示
# result = sum(variables[i].value() for i in range(N))
# print(int(result))


# 線形計画の定義 (整数計画問題)
problem = pulp.LpProblem("MaximizeDishes", pulp.LpMaximize)

# 変数の定義
x = pulp.LpVariable("x", 0, None, pulp.LpInteger)
y = pulp.LpVariable("y", 0, None, pulp.LpInteger)

# 目的関数の定義
problem += x + y

# 制約条件の定義
for i in range(N):
    problem += A[i] * x + B[i] * y <= Q[i]

# 問題を解く
problem.solve(pulp.PULP_CBC_CMD(msg=False))

print(int(pulp.value(problem.objective)))
