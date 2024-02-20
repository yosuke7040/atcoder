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


N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    x = A[i]
    tmp = 0

    for j in range(N):
        if A[j] >= x:
            tmp += x
            ans = max(ans, tmp)

        elif A[j] < x:
            tmp = 0

print(ans)
