#前計算

import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

def main():
    H, W = map(int, input().split())
    grids = []
    for i in range(H):
        grids.append(list(map(int, input().split())))

    total_row = [0] * H
    for i, row in enumerate(grids):
        total_row[i] = sum(row)

    total_col = [0] * W
    for i, column in enumerate(zip(*grids)):
        total_col[i] = sum(column)

    ans = [[0 for i in range(W)] for j in range(H)]
    for i in range(H):
        for j in range(W):
            ans[i][j] = total_row[i] + total_col[j] - grids[i][j]

        print(' '.join(str(ans[i][l]) for l in range(W)))

main()