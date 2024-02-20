import sys
sys.setrecursionlimit(10**6)
from itertools import product

S = input()
a, b = map(int, input().split())
print(S[:a-1]+S[b-1]+S[a:b-1]+S[a-1]+S[b:])


# なんでできないか思ったらpythonは文字列に対して代入できません！
# なのでリストで受け取る
# A = S
# S_a = S[a-1]
# S_b = S[b-1]

# ans = S
# print(ans, S_a, S_b)
# print(ans[a-1])

# ans[a-1] = S_b
# ans[b-1] = S_a
# print(ans)

# print(S[:a-1], S[b-1], S[a:b-1], S[a-1], S[b:])
