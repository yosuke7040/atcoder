import math
N = int(input())

# for i in range(2, int(math.sqrt(N))):
#     if N % i == 0:
#         print(i)

ans = []
target = N
# while target != 1:
#     for i in range(2, int(math.sqrt(target))):
#         if N % i == 0:
#             ans.append(i)
#             target = N//i
#             break
for i in range(2, int(N**0.5)):
    while N % i == 0:
        ans.append(i)
        N //= i
if N > 1:
    ans.append(N)

print(*ans)
# for i in ans:
#     print(i, end="")