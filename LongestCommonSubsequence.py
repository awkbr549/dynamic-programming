#! /usr/bin/python3

def lcs(x, y):
    m = len(x)
    n = len(y)
    T = []
    P = []
    for i in range(0, m+1):
        T.append([])
        P.append([])
        for j in range(0, n+1):
            T[i].append(None)
            P[i].append(None)

    for i in range(0, m+1):
        T[i][0] = 0
    for j in range(0, n+1):
        T[0][j] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if (x[i-1] == y[j-1]):
                T[i][j] = T[i-1][j-1] + 1
                P[i][j] = "di"
            elif (T[i][j-1] > T[i-1][j]):
                T[i][j] = T[i][j-1]
                P[i][j] = "le"
            else:
                T[i][j] = T[i-1][j]
                P[i][j] = "up"
    return T, P

def printLcs(P, x, i, j):
    if (i > 0 and j > 0):
        if (P[i][j] == "di"):
            rtrn = printLcs(P, x, i-1, j-1)
            print(x[i-1], end="")
        elif (P[i][j] == "le"):
            rtrn = printLcs(P, x, i, j-1)
        else:
            rtrn = printLcs(P, x, i-1, j)
    else:
        return

x = "atgcttgca"
y = "aggctgaa"

print(x)
print(y)
print()

T, P = lcs(x, y)
print("T: ")
for i in range(0, len(x)+1):
    print(T[i])
print()

print("P: ")
for i in range(0, len(x)+1):
    print(P[i])
print()

print("LCS: " + str(T[len(x)][len(y)]))
print()

print(x)
print(y)
printLcs(P, x, len(x), len(y))
print("\n")
