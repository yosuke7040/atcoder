def GCD(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
        
    if x < y:
        x, y = y, x
    x = x % y
    return GCD(x, y)

def LCM(x, y):
    return x*y//GCD(x,y)

N = int(input())
A = list(map(int, input().split()))
x = A[0]
for i in range(1, N):
    x = LCM(x, A[i])
# ans = GCD(A, B)
print(x)
