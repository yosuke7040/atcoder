import sys

sys.setrecursionlimit(10**6)

N = int(input())


def ten(x):
    x_str = str(x)
    for i in range(len(x_str)):
        if x_str[i] == "7":
            return True


def eight(x):
    x_str = str(oct(x))
    for i in range(len(x_str)):
        if x_str[i] == "7":
            return True


ans = 0
for i in range(1, N + 1):
    if ten(i) or eight(i):
        continue
    ans += 1

print(ans)
