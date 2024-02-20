import sys
sys.setrecursionlimit(10**6)
from itertools import product

S, T, X = map(int, input().split())

# isValid = [False]*24

# cnt = S
# while 1:
#     isValid[cnt] = True
#     cnt += 1
#     if cnt > 23:
#         cnt = 0
#     if cnt == T:
#         break

# if isValid[X]:
#     print("Yes")
# else:
#     print("No")

now = S
while S != T:
    if S == X:
        print("Yes")
        exit()
    S += 1
    S %= 24

print("No")