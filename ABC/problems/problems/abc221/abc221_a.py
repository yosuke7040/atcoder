import sys
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())

r = 0
r = abs(a - b)
if r == 0:
    print(1)
else:
    print(32**r)
