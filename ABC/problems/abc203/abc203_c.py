import sys

sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()

ans = K
for i in range(N):
    if AB[i][0] <= ans:
        ans += AB[i][1]

print(ans)
