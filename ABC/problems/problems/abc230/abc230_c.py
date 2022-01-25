import sys
sys.setrecursionlimit(10**6)
from itertools import product

N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())



for i in range(P, Q+1):
    row = []
    for j in range(R, S+1):
        if A+j == B+i or i+j == A+B:
            row.append("#")
        else:
            row.append(".")
    print("".join(row))


# first_left = max(1 - A, 1 - B)
# # print(f'first_left={first_left}')
# first_right = min(N - A, N - B)
# # print(f'first_right={first_right}')
# second_left = max(1- A, B - N)
# # print(f'second_left={second_left}')
# second_right = min(N - A, B - 1)
# # print(f'second_right={second_right}')
# # print(f'abs(R-S)+1)={abs(R-S)+1} (abs(P-Q)+1)={(abs(P-Q)+1)}')
# board = [['.'] * (abs(R-S)+1) for _ in range(abs(P-Q)+1)]
# # board = [['.'] * N for _ in range(N)]



# for k in range(first_left, first_right+1):
#     # print(k)
#     # print(f'A+k-1={A+k-1} B+k-1={B+k-1}')
#     if A+k <= 0 or A+k > N:
#         continue
#     if B+k <= 0 or B+k > N:
#         continue
#     board[A+k-1][B+k-1] = '#'

# # print('----------')
# for k in range(second_left, second_right+1):
#     if A+k <= 0 or A+k > N:
#         continue
#     if B-k <= 0 or B-k > N:
#         continue
#     # print(f'A+k-1={A+k-1} B-k-1={B-k-1}')
#     board[A+k-1][B-k-1] = '#'
#     # print(board)


# for i in range(P-1, Q):
#     # for j in range(abs(R-S)+1):
#     print(''.join(board[i][R-1:S]))