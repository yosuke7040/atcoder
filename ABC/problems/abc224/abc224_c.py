import sys
sys.setrecursionlimit(10**6)
from decimal import Decimal

n = int(input())
coordinate = [tuple(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            # x軸が全部一緒
            if coordinate[i][0] == coordinate[j][0] == coordinate[k][0]:
                continue
            # y軸が全部一緒
            if coordinate[i][1] == coordinate[j][1] == coordinate[k][1]:
                continue
            # 斜めが一直線 = 傾きが一緒
            x1, y1 = coordinate[i]
            x2, y2 = coordinate[j]
            x3, y3 = coordinate[k]
            x1 -= x3
            x2 -= x3
            y1 -= y3
            y2 -= y3
            if x1 * y2 == x2 * y1:
                continue

            cnt += 1

print(cnt)
