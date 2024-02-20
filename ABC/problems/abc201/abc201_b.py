import sys

sys.setrecursionlimit(10**6)

N = int(input())

mountains = []
for _ in range(N):
    S, T = map(str, input().split())
    mountains.append([int(T), S])

mountains.sort(reverse=True)
print(mountains[1][1])
