import sys
sys.setrecursionlimit(10**6)
from itertools import product

N, K = map(int, input().split())
A = list(map(int, input().split()))
# A = sorted(A)
# print(A)

# cnt = 0
# l = r = 0

# S = []
# for i in range(N+1):
#     S.append(sum(A[:i]))
# print(S)

# for l in range(N):
#     ans = A[l]
#     for r in range(l, N):
#         # ans = S[r] - S[l]
#         if l == r:
#             pass
#         else:
#             ans += A[r]

#         if ans == K:
#             cnt += 1

# print(cnt)

sum_cnt = {0:1}
accumulate = 0
ans = 0

for a in A:
    print('')
    accumulate += a
    l = accumulate - K
    print(f'a:{a} accumulate:{accumulate} l={l}')
    print(sum_cnt)
    if l in sum_cnt:
        print('yes')
        ans += sum_cnt[l]
        print(f'ans:{ans} sum_cnt[l]={sum_cnt[l]}')

    if accumulate not in sum_cnt:
        sum_cnt[accumulate] = 0
    sum_cnt[accumulate] += 1

print(sum_cnt)
print(ans)