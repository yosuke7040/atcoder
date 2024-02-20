import sys
sys.setrecursionlimit(10**6)
from decimal import Decimal
from itertools import product

# N = int(input())

# a = 1
# b = 1
# c = 1
# cnt = 0

# while 1:

#     # print('--------')
#     # print(a < b < c)
#     # print((a*b*c) <= N)
#     if (a <= b <= c) and (a*b*c) <= N:
        
#         cnt += 1

#     c += 1
#     if c > N:
#         c = 1
#         b += 1
#         if b > N:
#             a += 1
#             if a > N:
#                 break
    
# print(cnt)

N = int(input())

cnt = 0
for a in range(1, N+1):
    if a*a*a > N:
        break

    for b in range(a, N+1):
        if b*b*a > N:
            break

        # 1 <= C <= N/AB^2
        # print(a, b)
        cnt += (N // (a*b)) - b + 1
print(cnt)
