#! /usr/bin/python3

def assemblyLine(a, t, e, x, n):
    M = [[], [], []]
    P = [[], [], []]
    for i in range(0, n+1):
        M[0].append("inf")
        M[1].append(None)
        M[2].append(None)

        P[0].append("inf")
        P[1].append(None)
        P[2].append(None)

    M[1][1] = e[1] + a[1][1]
    M[2][1] = e[2] + a[2][1]
    for j in range(2, n+1):
        if (M[1][j-1] + a[1][j] <= M[2][j-1] + t[2][j-1] + a[1][j]):
            M[1][j] = M[1][j-1] + a[1][j]
            P[1][j] = 1
        else:
            M[1][j] = M[2][j-1] + t[2][j-1] + a[1][j]
            P[1][j] = 2
        if (M[2][j-1] + a[2][j] <= M[1][j-1] + t[1][j-1] + a[2][j]):
            M[2][j] = M[2][j-1] + a[2][j]
            P[2][j] = 2
        else:
            M[2][j] = M[1][j-1] + t[1][j-1] + a[2][j]
            P[2][j] = 1

    return M, P, min(M[1][n] + x[1], M[2][n] + x[2])

def printPathMain(M, P, minimum, x, n):
    if (minimum - x[1] == M[1][n]):
        i = 1
    else:
        i = 2
    printPath(P, i, n)

def printPath(P, i, j):
    if (j >= 1):
        printPath(P, P[i][j], j-1)
        print(str([i, j]))

a = [["inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf"],
     ["inf", 7, 9, 3, 4, 8, 4, 12, 6, 4],
     ["inf", 8, 5, 6, 4, 5, 7, 3, 13, 7]]
t = [["inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf"],
     ["inf", 2, 3, 1, 3, 4, 1, 2, 3],
     ["inf", 2, 1, 2, 2, 1, 4, 1, 2]]
e = ["inf", 2, 4]
x = ["inf", 3, 2]
n = 9

M, P, minimum = assemblyLine(a, t, e, x, n)
print(minimum)
print()

printPathMain(M, P, minimum, x, n)
