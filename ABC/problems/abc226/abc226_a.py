import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

# X = float(input())
# r_X = round(X)

# if X > 0:
#     if r_X  == 0:
#         print(1)
#     else:
#         print(r_X)
# else:
#     print(r_X)
# # print(round(X))
# # print(format(X, '.0f'))

# print(Decimal(input()).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

x, y = map(int, input().split('.'))
if y < 500:
    print(x)
else:
    print(x+1)