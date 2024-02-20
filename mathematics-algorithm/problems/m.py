import math
N = int(input())
# print(N)
# print(int(math.sqrt(N)))

for i in range(1, int(math.sqrt(N))+1):
    # print("mod={}".format(N % i))
    if N % i == 0:
        print(i)
        if i != N / i:
            print(N // i)


