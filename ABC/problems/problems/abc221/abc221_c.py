# bit全探索
import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product


n = input()
ans = 0

for bits in product((0,1), repeat=len(n)):
    first = []
    second = []
    for i, bit in enumerate(bits):
        if bit:
            first.append(n[i])
        else:
            second.append(n[i])

    if len(first) == 0 or len(second) == 0:
        continue

    first.sort(reverse=True)
    second.sort(reverse=True)

    f = int("".join(first))
    s = int("".join(second))
    ans = max(ans, f*s)

print(ans)
