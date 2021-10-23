import sys
sys.setrecursionlimit(10**6)
import copy
from itertools import product

def shift_words(words, i):
    ans = words[i:] + words[:i]
    return ans

s = input()

shift_list = []
for i in range(len(s)):
    # if i == 0:
    #     shift_list.append(s)
    # else:
        shift_list.append(shift_words(s, i))

shift_list.sort()
print(shift_list[0])
print(shift_list[-1])