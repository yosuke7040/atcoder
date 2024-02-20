import sys

sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

# print(sorted(str(N)))
# print(int("".join(sorted(str(N)))))
# print(sorted(str(N), reverse=True))


def g1(x):
    return int("".join(sorted(str(x), reverse=True)))


def g2(x):
    return int("".join(sorted(str(x))))


def f(x):
    return g1(x) - g2(x)


a = N
for i in range(K):
    # print(a)
    a = f(a)

print(a)
