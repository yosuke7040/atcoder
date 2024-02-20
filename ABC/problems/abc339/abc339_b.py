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


H, W, N = map(int, input().split())


grid = [list() for _ in range(H)]
for i in range(H):
    for j in range(W):
        grid[i].append(".")

# print(grid)
dist = "up"
place = [0, 0]
for i in range(N):
    if grid[place[0]][place[1]] == ".":
        grid[place[0]][place[1]] = "#"

        if dist == "up":
            dist = "right"
            place[1] += 1
            if place[1] == W:
                place[1] = 0
        elif dist == "down":
            dist = "left"
            place[1] -= 1
            if place[1] == -1:
                place[1] = W - 1
        elif dist == "right":
            dist = "down"
            place[0] += 1
            if place[0] == H:
                place[0] = 0
        elif dist == "left":
            dist = "up"
            place[0] -= 1
            if place[0] == -1:
                place[0] = H - 1

    else:
        grid[place[0]][place[1]] = "."

        if dist == "up":
            dist = "left"
            place[1] -= 1
            if place[1] == -1:
                place[1] = W - 1
        elif dist == "down":
            dist = "right"
            place[1] += 1
            if place[1] == W:
                place[1] = 0
        elif dist == "right":
            dist = "up"
            place[0] -= 1
            if place[0] == -1:
                place[0] = H - 1
        elif dist == "left":
            dist = "down"
            place[0] += 1
            if place[0] == H:
                place[0] = 0

    # print("------- i:", i)
    # for i in range(H):
    #     print("".join(grid[i]))

for i in range(H):
    print("".join(grid[i]))
