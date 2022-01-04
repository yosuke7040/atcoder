from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)

cnt = 0
while len(C) > 0:
    for v in C:
        a = C[v]
        b = C[500-v]
        cnt += a*b
        del C[v]
        del C[500-v]
        break

print(cnt)    