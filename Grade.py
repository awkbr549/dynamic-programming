#! /usr/bin/python3

def grade(x, y):
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

    T[0][0] = 0
    for i in range(0, m+1):
        T[i][0] = -3 * i
    for j in range(0, n+1):
        T[0][j] = -3 * j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if (x[i-1] == y[j-1]):
                T[i][j] = T[i-1][j-1] + 5
                P[i][j] = 1
            else:
                if (T[i-1][j-1] - 2 > T[i][j-1] - 3):
                    if (T[i-1][j-1] - 2 > T[i-1][j] - 3):
                        T[i][j] = T[i-1][j-1] - 2
                        P[i][j] = 2
                    else:
                        T[i][j] = T[i-1][j] - 3
                        P[i][j] = 4
                else:
                    if (T[i][j-1] - 3 > T[i-1][j] - 3):
                        T[i][j] = T[i][j-1] - 3
                        P[i][j] = 3
                    else:
                        T[i][j] = T[i-1][j] - 3
                        P[i][j] = 4
    return T, P

x = "The earth is flat!"
y = "The Earth is round."

print(x)
print(y)
print()

T, P = grade(x, y)
print("T: ")
for i in range(0, len(x)+1):
    print(T[i])
print()

print("P: ")
for i in range(0, len(x)+1):
    print(P[i])
print()

print("Grade: " + str(T[len(x)][len(y)]))
print()

'''
print(x)
print(y)
printLcs(P, x, len(x), len(y))
print("\n")
'''
