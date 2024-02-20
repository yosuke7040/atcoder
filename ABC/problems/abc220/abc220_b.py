from sys import stdin

n = int(input())
A, B = stdin.readline().rstrip().split()
print(int(A, n) * int(B, n))
