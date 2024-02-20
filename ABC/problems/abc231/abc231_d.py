import sys
sys.setrecursionlimit(10**6)
from itertools import product
class UnionFind():
    def __init__(self, n):
        self.par = [-1] * n
        self.siz = [1] * n
        self.rank = [0] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        
        if self.rank[ry] > self.rank[rx]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        
        self.siz[rx] += self.siz[ry]
        return True

    def size(self, x):
        return self.siz[self.root(x)]


N, M = map(int, input().split())
ans = [0]*N
uf = UnionFind(N)


for i in range(M):
    A, B = map(int ,input().split())
    ans[A-1] += 1
    ans[B-1] += 1

    if uf.unite(A-1, B-1):
        pass
    else:
        print("No")
        exit()

# if max(ans) >= 3:
#     print("No")
#     exit()

for i in range(M):
    if uf.size(i) >= 4:
        print("No")
        exit()

print("Yes")
    