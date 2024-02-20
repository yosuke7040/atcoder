import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

s = input()
er_tail = s[-2:]

if er_tail == "er":
    print("er")
else:
    print("ist")