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


# N, X = map(int, input().split())

# drunk = 0
# X = X * 100
# for i in range(N):
#     V, P = map(int, input().split())

#     alcohol = V * P
#     drunk += alcohol

#     if drunk > X:
#         print(i + 1)
#         exit()

# print(-1)

N, X = map(int, input().split())
X = X * 100
total = 0
for i in range(N):
    V, P = map(int, input().split())
    total += V * P

    # print(total)
    # print(X)
    if total > X:
        print(i + 1)
        exit()

print(-1)
