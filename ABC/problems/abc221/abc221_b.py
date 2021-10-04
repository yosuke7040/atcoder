import sys
sys.setrecursionlimit(10**6)

S = input()
T = input()

if S == T:
    print("Yes")
    sys.exit()
else:
    S = list(S)
    T = list(T)
    for i in range(100):
        if S[i] == T[i]:
            continue
        else:
            tmp = ""
            tmp = S[i]
            S[i] = S[i+1]
            S[i+1] = tmp
            break

if S == T:
    print("Yes")
else:
    print("No")
