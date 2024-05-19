import sys

sys.setrecursionlimit(10**6)


from heapq import heapify, heappop, heappush

N, K = map(int, input().split())
P = list(map(int, input().split()))

pq = P[:K]
heapify(pq)
print(pq[0])

for i in range(N - K):
    heappush(pq, P[K + i])
    heappop(pq)
    print(pq[0])


# ans = [False] * (N+1)
# for i in range(K):
#     ans[P[i]] = True

# ahead = sorted(P[:K], reverse=True)
# min = ahead[K-1]
# print(min)

# for i in range(N - K):
#     ans[P[K+i]] = True
#     if P[K+i] > min:
#         while 1:
#             min += 1
#             if ans[min]:
#                 print(min)
#                 break
#     else:
#         print(min)


# def val_insert(ans, x):
#     l = 0
#     r = len(ans)
#     while l < r:
#         mid = (l + r) // 2
#         if ans[mid] >= x:
#             l = mid+1
#         else:
#             r = mid
#     ans.insert(l, x)

# for i in range(N - K + 1):
#     ans = sorted(P[:K+i], reverse=True)
#     print(ans[K-1])


# ans = sorted(P[:K], reverse=True)
# print(ans[K-1])
# min_ans = ans[K-1]

# for i in range(N - K):
#     # 2分探索
#     if min_ans > P[K+i]:
#         print(ans[K-1])
#         continue

#     # val_insert(ans, P[K+i])
#     l = 0
#     r = len(ans)
#     while l < r:
#         mid = (l + r) // 2
#         if ans[mid] >= P[K+i]:
#             l = mid+1
#         else:
#             r = mid
#     ans.insert(l, P[K+i])

#     print(ans[K-1])


# print(ans)
