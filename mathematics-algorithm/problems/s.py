from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)

cnt = 0
for key in C:
    value = C[key]
    cnt += (value*(value-1)//2)
print(cnt)    