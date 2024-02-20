import sys
sys.setrecursionlimit(10**6)
from itertools import product

K = int(input())
bin_K = bin(K)
bin_K_str = str(bin_K)
# print(bin_K_str)
# print(len(bin_K_str)+1)

ans = []
for i in range(2, len(bin_K_str)):
    if bin_K_str[i] == '1':
        ans.append('2')
    else:
        ans.append('0')

for i in range(len(ans)):
    print(ans[i], end='')
print('')