from collections import Counter
from itertools import product, combinations

n, r = map(int, input().split())

numerator =  denominator = 1

for i in range(r):
    numerator *= n - i
    denominator *= i+1

# print(numerator, denominator)
print(numerator//denominator)