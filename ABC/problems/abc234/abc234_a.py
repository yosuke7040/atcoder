import sys
sys.setrecursionlimit(10**6)
from itertools import product

def f(x):
    return x**2 + 2*x + 3

t = int(input())
print(f(f(f(t) + t) + f(f(t))))