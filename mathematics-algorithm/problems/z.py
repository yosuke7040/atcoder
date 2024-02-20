from collections import Counter
from itertools import product, combinations

N = int(input())

ans = 1
for i in range(1, N):
    ans += (1 / (1 - (i/N)))

print(ans)