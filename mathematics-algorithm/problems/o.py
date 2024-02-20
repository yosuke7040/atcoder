def GCD(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
        
    if x < y:
        x, y = y, x
    x = x % y
    return GCD(x, y)

A, B  = map(int, input().split())
ans = GCD(A, B)
print(ans)
