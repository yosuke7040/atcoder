import sys
sys.setrecursionlimit(10**6)
from itertools import product

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()


for i in range(Q):
    x = int(input())
    left = 0
    right = N
    while left < right:
        mid = (left+right) // 2
        if A[mid] == x:
            left = mid
            break
        elif A[mid] > x:
            right = mid
        else:
            left = mid + 1
    
    # print(f"left={left}")
    if left == N:
        print(0)
    elif A[left] == x:
        print(N-left)
    else:
        print(N-left)
