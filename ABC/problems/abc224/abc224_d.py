import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

m = int(input())
band = [tuple(map(int, input().split())) for _ in range(m)]
p = [tuple(map(int, input().split()))]

