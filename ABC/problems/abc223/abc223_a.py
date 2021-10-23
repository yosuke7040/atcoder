import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

x = int(input())

if x >= 100:
    if x % 100 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")