from collections import Counter
from itertools import product, combinations

N = int(input())
A = list(map(int, input().split()))

# cnt = 0
# C = Counter(A)
# print(C)
# for select in combinations(C, 2):
#     if select[0] + select[1] == 100000:
#         print(C[select[0]], C[select[1]])
#         cnt += C[select[0]] * C[select[1]]

cnt = [0 for i in range(100000)]
for i in range(N):
    cnt[A[i]] += 1

ans = 0
for i in range(1, 50000):
    ans += cnt[i] * cnt[100000 - i]
ans += cnt[50000] * (cnt[50000] - 1) // 2

print(ans)