import sys

sys.setrecursionlimit(10**6)

H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
if S[X - 1][Y - 1] == ".":
    ans += 1


def left():
    count = 0
    for i in range(1, W):
        if Y - i == 0:
            break

        if S[X - 1][Y - 1 - i] == ".":
            count += 1
        else:
            break
    return count


def right():
    count = 0
    for i in range(1, W):
        if Y + i > W:
            break

        if S[X - 1][Y - 1 + i] == ".":
            count += 1
        else:
            break
    return count


def up():
    count = 0
    for i in range(1, H):
        if X - i == 0:
            break

        if S[X - 1 - i][Y - 1] == ".":
            count += 1
        else:
            break
    return count


def down():
    count = 0
    for i in range(1, H):
        if X + i > H:
            break

        if S[X - 1 + i][Y - 1] == ".":
            count += 1
        else:
            break
    return count


# print(left(), right(), up(), down())
ans += left() + right() + up() + down()
print(ans)
