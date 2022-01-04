from collections import Counter
from itertools import product, combinations

N = int(input())
A = list(map(int, input().split()))
# C = Counter(A)

cnt = 0
for select in combinations(A, 5):
    # if sum(select) == 1000:
    ans = 0
    for x in select:
        ans += x
    if ans == 1000:
        cnt += 1

print(cnt)