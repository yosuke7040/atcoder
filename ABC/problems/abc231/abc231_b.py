import sys
sys.setrecursionlimit(10**6)
from itertools import product
import collections

N = int(input())
names = []
for i in range(N):
    names.append(input())
c = collections.Counter(names)

print(c.most_common()[0][0])