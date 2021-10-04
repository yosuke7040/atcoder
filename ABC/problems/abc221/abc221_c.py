import sys
sys.setrecursionlimit(10**6)
import copy

N = ""
N = str(input())
N_list = list(N)

max_value = 0
x = []
y = []
x_val = 0
y_val = 0


for i in range(len(N)//2):
    y = []
    x = []
    org_N_list = copy.copy(N_list)

    for j in range(i+1):
        x.append(max(org_N_list))
        org_N_list.remove(max(org_N_list))
        y.append(max(org_N_list))
        org_N_list.remove(max(org_N_list))

    if org_N_list:
        y += org_N_list

    x_val = int("".join(sorted(x, reverse=True)))
    y_val = int("".join(sorted(y, reverse=True)))
    if (x_val * y_val) > max_value:
        max_value = (x_val * y_val)

print(max_value)
