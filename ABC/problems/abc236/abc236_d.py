import sys
sys.setrecursionlimit(10**6)
from itertools import product, permutations, combinations

N = int(input())
# print(people)
# A = []
# for i in range((N*2)-1):
#     A.append(list(map(int, input().split())))

for pare in permutations(list(range(N*2)), 2):
    print(pare)
print("------------------------")
# max_score = 0
people = list(range(N*2))
for pare in combinations(people, N):
    print(pare)
#     # a = bin(A[pare[0]][pare[1]])

A = [[0]*(2*N+1) for _ in range(2*N+1)]

for i in range(1, 2*N):
    a_list = list(map(int, input().split()))
    for j, a in enumerate(a_list):
        A[i][i+1+j] = a
        A[i+1+j][i] = a

ans = 0
selected = [False]*(2*N+1)
pairs = []


def DFS(selected, pairs):
    global ans

    if len(pairs) == 2*N:
        score = 0
        for i in range(0, 2*N, 2):
            x = pairs[i]
            y = pairs[i+1]

            score ^= A[x][y]

        ans = max(score, ans)

    elif len(pairs) % 2 == 0:
        i = 1
        while selected[i] == True:
            i += 1
        pairs.append(i)
        selected[i] = True
        DFS(selected, pairs)
        pairs.pop()
        selected[i] = False

    else:
        for i in range(1, 2*N+1):
            if selected[i] == False:
                pairs.append(i)
                selected[i] = True
                DFS(selected, pairs)
                pairs.pop()
                selected[i] = False

        

DFS(selected, pairs)

print(ans)
