# a, b, c = [*map(int, input().split())]
# if a > c:
#     anser = a + (c - (a % c))
# else:
#     anser = c
# if anser > b:
#     anser = -1
# print(anser)

A, B, C = map(int, input().split())
for i in range(1, 1000):
    if A <= (C * i) <= B:
        print(C * i)
        exit()

print(-1)
