import sys
sys.setrecursionlimit(10**6)
from itertools import product

S = input()
T = 'oxx' * 10

# isOk = False

# if len(S) == 1:
#     if S[0] == 'o' or S[0] == 'x':
#         isOk = True
    
# elif len(S) == 2:
#     if S == 'ox' or S == 'xx' or S == 'xo':
#         isOk = True

# else:
#     if S[0] == 'o':
#         idx = 0
#     elif S[0] == 'x':
#         if S[1] == 'x':
#             idx = 1
#         else:
#             idx = 2
#     isOk = True
#     for i in range(len(S)):
#         if S[i] != T[i + idx]:
#             isOk = False
#             break


# if isOk:
#     print('Yes')
# else:
#     print('No')

print("Yes" if S in T else "No")