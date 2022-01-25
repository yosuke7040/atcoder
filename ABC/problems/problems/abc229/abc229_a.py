import sys
sys.setrecursionlimit(10**6)
from itertools import product

S1 = input()
S2 = input()

if S1[0] == S2[0]:
    print("Yes")
elif S1[0] == S1[1]:
    print("Yes")
elif S1[1] == S2[1]:
    print("Yes")
elif S2[0] == S2[1]:
    print("Yes")
else:
    print("No")