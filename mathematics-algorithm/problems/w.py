from collections import Counter
from itertools import product, combinations

N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

B_expect = sum(B) / N
R_expect = sum(R) / N

print(B_expect + R_expect)