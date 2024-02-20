import math
import sys

sys.setrecursionlimit(10**6)

N = int(input())

# print(math.sqrt(N))
# print(math.ceil(math.sqrt(N)))

ans = set()
for i in range(1, math.ceil(math.sqrt(N)) + 1):
    if N % i == 0:
        # print(i, N // i)
        ans.add(i)
        ans.add(N // i)

for x in sorted(ans):
    print(x)
