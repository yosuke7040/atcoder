import sys

sys.setrecursionlimit(10**6)
INF = 1 << 60


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


N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = set()
A_dict = dict()
B_dict = dict()
for i in range(N):
    A_dict[i + 1] = A[i]
    B_dict[i + 1] = B[i]

A_dict_sort = sorted(A_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)
B_dict_sort = sorted(B_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)

# print("=========1===========")
# print(A_dict_sort)
# print(B_dict_sort)
# print(ans)
# 数学高い順
for i in range(X):
    ans.add(A_dict_sort[i][0])
    A_dict.pop(A_dict_sort[i][0])
    B_dict.pop(A_dict_sort[i][0])


A_dict_sort = sorted(A_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)
B_dict_sort = sorted(B_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)
# print("=========2===========")
# print(A_dict_sort)
# print(B_dict_sort)
# print(ans)

# 英語高い順
for i in range(Y):
    ans.add(B_dict_sort[i][0])
    A_dict.pop(B_dict_sort[i][0])
    B_dict.pop(B_dict_sort[i][0])

# print("=========3===========")
# print(A_dict_sort)
# print(B_dict_sort)
# print(ans)

A_dict_sort = sorted(A_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)
B_dict_sort = sorted(B_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)

# 両方高い順
ryouhou = dict()
for i in range(len(A_dict_sort)):
    for j in range(len(B_dict_sort)):
        if A_dict_sort[i][0] == B_dict_sort[j][0]:
            ryouhou[A_dict_sort[i][0]] = A_dict_sort[i][1] + B_dict_sort[j][1]

ryouhou_sort = sorted(ryouhou.items(), key=lambda x: (x[1], -x[0]), reverse=True)
# print("=========4===========")
# print(A_dict_sort)
# print(B_dict_sort)
# print(ans)
# print(ryouhou_sort)
for i in range(Z):
    ans.add(ryouhou_sort[i][0])

# print("=========5===========")
tmp_ans = list(ans)
# print(tmp_ans)
# print(ans)
tmp_ans.sort()
for i in range(len(tmp_ans)):
    print(tmp_ans[i])

# print("!!!!!!!!!!!!!!!!!!")
# import random

# hoge = set()
# for i in range(10):
#     hoge.add(random.randint(1, 100))

# print(hoge)

# for i in range(20):
#     hoge.add(random.randint(1, 100))

# print(hoge)

# fuga = set()
# fuga.add(1)
# fuga.add(3)
# fuga.add(2)
# print(fuga)
