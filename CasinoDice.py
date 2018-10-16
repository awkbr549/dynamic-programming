#! /usr/bin/python3

def casinoDice(a, t, e, n):
    M = [[], [], []]
    P = [[], [], []]
    for i in range(0, n+1):
        M[0].append("-inf")
        M[1].append(None)
        M[2].append(None)

        P[0].append("-inf")
        P[1].append(None)
        P[2].append(None)

    M[1][1] = e[1] * probA(a, 1, 1)
    M[2][1] = e[2] * probA(a, 2, 1)

    for j in range(2, n+1):
        if (M[1][j-1] * t[1][1] * probA(a, 1, j)
            >= M[2][j-1] * t[2][1] * probA(a, 1, j)
        ):
            M[1][j] = M[1][j-1] * t[1][1] * probA(a, 1, j)
            P[1][j] = 1
        else:
            M[1][j] = M[2][j-1] * t[2][1] * probA(a, 1, j)
            P[1][j] = 2
        if (M[2][j-1] * t[2][2] * probA(a, 2, j)
            >= M[1][j-1] * t[1][2] * probA(a, 2, j)
        ):
            M[2][j] = M[2][j-1] * t[2][2] * probA(a, 2, j)
            P[2][j] = 2
        else:
            M[2][j] = M[1][j-1] * t[1][2] * probA(a, 2, j)
            P[2][j] = 1

    return M, P, max(M[1][n], M[2][n])

def probA(a, i, j):
    result = 1.0 / 6.0
    if (i == 2):
        if (a[j] == 6):
            result = 1.0 / 2.0
        else:
            result = 1.0 / 10.0
    return result

def printPathMain(M, P, maximum, n):
    if (maximum == M[1][n]):
        i = 1
    else:
        i = 2
    printPath(P, i, n)

def printPath(p, i, j):
    if (j >= 1):
        printPath(P, P[i][j], j-1)
        print(str([i, j]))

a = ["-inf", 6, 6, 6, 1, 2, 3, 4]
t = [["-inf", "-inf", "-inf"],
     ["-inf", 0.95, 0.05],
     ["-inf", 0.9, 0.1]]
e = ["-inf", 0.5, 0.5]
n = 7
M, P, maximum = casinoDice(a, t, e, n)
print(maximum)

for i in range(1, len(M)):
    print(M[i][1:])

printPathMain(M, P, maximum, n)
