# 答えで２分探索

import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

left = 0
right = L
ans = 0
num_piece = 0
mid = 0

split_A = []
pre = 0
for i in range(N):
    split_A.append(A[i] - pre)
    pre = A[i]
split_A.append(L-A[N-1])

def calc(threshold):
    global left
    global right
    global ans
    num_piece = 0
    length = 0

    for i in range(len(split_A)):
        length += split_A[i]
        if length >= threshold:
            num_piece += 1
            length = 0
    # 残り部分は閾値より低くなってないか
    if length == 0:
        pass
    elif length < threshold:
        pass
    else:
        num_piece += 1

    if num_piece < K+1:
        right = threshold
    else:
        ans = threshold
        left = threshold + 1
  

cnt = 0
while( left < right ):
    mid = (right + left) // 2
    calc(mid)
            

print(ans)