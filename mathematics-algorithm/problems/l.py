import math
N = int(input())

cnt = 0
for i in range(2, int(math.sqrt(N))):
    if N % i == 0:
        cnt += 1

if cnt > 0:
    print("No")
else:
    print("Yes")
