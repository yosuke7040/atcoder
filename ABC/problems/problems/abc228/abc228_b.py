import sys
sys.setrecursionlimit(10**6)
from itertools import product

N, X = map(int, input().split())
# A = list(map(int, input().split()))
# A.insert(0, 0)

# s = set()
# s.add(X)
# cnt = 1

# idx = X
# for _ in range(N):
#     if A[idx] in s:
#         break
    
#     s.add(A[idx])
#     idx = A[idx]
#     cnt += 1

# print(cnt)

a = [-1] + list(map(int, input().split()))

known = [False] * (N+1)

while not known[X]:
    known[X] = True
    X = a[X]

print(sum(known))