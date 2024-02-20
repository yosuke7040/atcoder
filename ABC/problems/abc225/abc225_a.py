import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

S = input()
cnt = 0
if S[0] == S[1]:
    cnt += 1
if S[0] == S[2]:
    cnt += 1
if S[1] == S[2]:
    cnt += 1

if cnt == 3:
    print("1")
elif cnt == 1:
    print("3")
elif cnt == 0:
    print("6")
