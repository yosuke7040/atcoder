import sys
sys.setrecursionlimit(10**6)
from itertools import product

N, X = map(int, input().split())
L = []
L_a_list = []
for i in range(N):
    tmp = list(map(int, input().split()))
    L.append(tmp[0])
    # L_a_list.append(sorted(tmp[1:]))
    L_a_list.append(tmp[1:])

# print(f'L={L}')
# print(f'L_a_list={L_a_list}')
# print(f'L_a_list={L_a_list}')

cnt = 0

for x in product(*L_a_list):
    ans = 1
    for i in x:
        ans *= i
    
    # print(ans)
    if ans == X:
        cnt += 1

print(cnt)