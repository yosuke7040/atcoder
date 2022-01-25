import sys
sys.setrecursionlimit(10**6)
from itertools import product

abc = input()

ans = 0
ans += int(abc[0]) + int(abc[1]) * 10 + int(abc[2]) * 100
ans += int(abc[1]) + int(abc[2]) * 10 + int(abc[0]) * 100
ans += int(abc[2]) + int(abc[0]) * 10 + int(abc[1]) * 100

print(ans)
