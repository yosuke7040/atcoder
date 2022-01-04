import sys
sys.setrecursionlimit(10**6)
from itertools import product

_A, _B = map(int, input().split())
A = str(_A)
B = str(_B)

isKuriagari = False
for i in range(min(len(A), len(B))):
    i = -(i+1)
    # print(i)
    a = int(A[i])
    b = int(B[i])
    # print(a, b)
    if a + b < 10:
        pass
    else:
        isKuriagari =True
        break

if isKuriagari:
    print("Hard")
else:
    print("Easy")
