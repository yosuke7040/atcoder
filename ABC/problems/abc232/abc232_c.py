import sys
sys.setrecursionlimit(10**6)
from itertools import product, permutations

N, M = map(int, input().split())
takahasi = [[False]*N for _ in range(N)]
aoki = [[False]*N for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    takahasi[a-1][b-1] = takahasi[b-1][a-1] = True

for i in range(M):
    c, d = map(int, input().split())
    aoki[c-1][d-1] = aoki[d-1][c-1] = True

for order in permutations(range(N)):
    isNotSame = False
    
    for i in range(N):
        for j in range(N):
            if takahasi[i][j] != aoki[order[i]][order[j]]:
                isNotSame = True
    if not isNotSame:
        print("Yes")
        exit()


print("No")

# takahasi = [0]*(N+1)
# for i in range(M):
#     # print(AB[i])
#     takahasi[AB[i][0]] += 1
#     takahasi[AB[i][1]] += 1

# aoki = [0]*(N+1)
# for i in range(M):
#     aoki[CD[i][0]] += 1
#     aoki[CD[i][1]] += 1

# takahasi.sort()
# aoki.sort()
# # print(takahasi)
# # print(aoki)

# if takahasi == aoki:
#     print("Yes")
# else:
#     print("No")
