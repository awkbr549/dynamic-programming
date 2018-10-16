#! /usr/bin/python3

def knapsack01(s, v, B, n):

    V = []
    P = []
    A = set()
    for i in range(0, n+1):
        V.append([])
        P.append([])
        for j in range(0, B+1):
            V[i].append(None)
            P[i].append([])

    for j in range(0, B+1):
        V[0][j] = 0
    for i in range(0, n+1):
        V[i][0] = 0

    for i in range(1, n+1):
        #print("object: " + str(i))
        for j in range(1, B+1):
            '''
            print("\tsize: " + str(j))
            print("\t\t" + str(j) + " >= " + str(s[i]) + ": " + str(j >= s[i]))
            '''
            if (j >= s[i]):
                V[i][j] = max(V[i-1][j-s[i]] + v[i], V[i-1][j])
                if (V[i][j] == V[i-1][j-s[i]] + v[i]):
                    P[i][j] = [i-1, j-s[i]]
                else:
                    P[i][j] = [i-1, j]
            else:
                V[i][j] = V[i-1][j]
                P[i][j] = [i-1, j]

            '''
            if (j >= s[i]):
                V[i][j] = V[i-1][j-s[i]] + v[i]
                P[i][j] = 1
            else:
                V[i][j] = V[i-1][j]
                P[i][j] = 2
            print("\t\tV[i][j]: " + str(V[i][j]))
            '''
                
    return V, P, V[n][B]
            
def printObjects(P, i, j):
    if (i >= 1 and j >= 1):
        if (P[i][j][1] != j):
            print(i, end=" ")
            #print(P[i][j])
        printObjects(P, P[i][j][0], P[i][j][1])

s = ["-inf", 3, 5, 3, 2]
v = ["-inf", 50, 40, 40, 10]
B = 10
n = 4
V, P, maxValue = knapsack01(s, v, B, n)
for i in range(0, n+1):
    print(V[i])
print()
'''for i in range(0, n+1): 
    print(P[i])'''
print("Objects added to knapsack: ", end="")
printObjects(P, n, B)
print()
print("Value: " + str(maxValue))

