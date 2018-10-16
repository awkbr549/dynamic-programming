#! /usr/bin/python3

import math
from random import randint
from random import uniform

USE_G = False

'''
g = [
    [math.inf, 5,        9,        math.inf, math.inf],
    [5,        math.inf, 2,        7,        math.inf],
    [9,        2,        math.inf, 3,        math.inf],
    [math.inf, 7,        3,        math.inf, 11],
    [math.inf, math.inf, math.inf, 11,       math.inf]
]
'''

'''
g = [
    [math.inf, 23, 17, 25, 90],
    [23, math.inf, 15, 7, 10],
    [17, 15, math.inf, 28, 17],
    [25, 7, 28, math.inf, 6],
    [90, 10, 17, 6, math.inf]
    ]
'''

n = 100
if (USE_G):
    n = len(g)
s = 0
t = n-1
MIN_RANDOM_TIME = 5
MAX_RANDOM_TIME = 20
MULTI_CHANGE_PROB = min(1 - (math.e**(-n/25)), 0.99)
NO_PATH_PROB = 0.05

def makeRandomGraph():
    g = []
    CONNECTIVITY = math.ceil(10 * (1 - (math.e**(-n/33.3333))))
    for i in range(0, n):
        g.append([])
        for j in range(0, n):
            g[i].append(math.inf)
    
    for i in range(0, n):
        for j in range(i+1, min(math.floor(n/CONNECTIVITY)+i, n)):
            if (uniform(0.0, 1.0) < NO_PATH_PROB):
                g[i][j] = math.inf
            else:
                g[i][j] = randint(MIN_RANDOM_TIME, MAX_RANDOM_TIME)

    for i in range(0, len(g)):
        for j in range(0, len(g[i])):
            if (i == j):
                g[i][j] = math.inf
            g[j][i] = g[i][j]

    return g

def printGraph(g):
    for i in range(0, len(g)):
        for j in range(0, len(g[i])):
            print(str(g[i][j]), end="")
            if (j < len(g[i])-1):
                print(",", end="")
                print("\t", end="")
        print()

def dijkstra(g, edge_info, s):
    for i in range(0, len(g)):
        edge_info[i][0] = math.inf
        edge_info[i][1] = None
    edge_info[s][0] = 0
    Q = set()
    for i in range(0, len(g)):
        Q.add(i)
    while Q:
        u, Q = extract_min(Q, edge_info)
        for v in range(0, len(g[u])):
            if (edge_info[v][0] > edge_info[u][0] + g[u][v]):
                edge_info[v][0] = edge_info[u][0] + g[u][v]
                edge_info[v][1] = u
    return edge_info

#extract edge with minimum distance edge_info[v][0]
def extract_min(Q, edge_info):
    min = None
    if (not (Q is None or edge_info is None)):
        for i in range(0, len(edge_info)):
            if (set([i]).issubset(Q)):
                if (min is None):
                    min = i
                elif (edge_info[i][0] < edge_info[min][0]):
                    min = i
        Q.remove(min)
    return min, Q

def makePath(edge_info, s, t):
    path = []
    y = t
    while (not edge_info[y][1] is None):
        path.insert(0, [edge_info[y][1], y])
        y = edge_info[y][1]
    return path

def printPath(path):
    print("\t" + str(path[0][0]) + " --> ", end="")
    for i in range(0, len(path)):
        print(str(path[i][1]), end="")
        if (i < len(path)-1):
            print(" --> ", end="")
    print()

def dynamicShortestPath(g, edge_info, path, w):
    if (shouldRecalculate(g, path, w)):
        print("\tRecalculating...")
        for change in w:
            u = change[0]
            v = change[1]
            newDist = change[2]
            g[u][v] = newDist
            g[v][u] = newDist
        
        x = path[0][0] #the first vertex in the path
        y = path[len(path)-1][1] #the last vertex in the path
        edge_info = dijkstra(g, edge_info, x)
        path = makePath(edge_info, x, y)
    for change in w:
        u = change[0]
        v = change[1]
        newDist = change[2]
        g[u][v] = newDist
        g[v][u] = newDist
    #g[u][v] = w
    #g[v][u] = w
    return edge_info, path

def shouldRecalculate(g, path, w):
    res = False
    for change in w:
        u = change[0]
        v = change[1]
        newDist = change[2]
        inPath = isInPath(u, v, path)
        if ((newDist < g[u][v] and not inPath) or (newDist > g[u][v] and inPath)):
            res = True
            break
    return res

def isInPath(u, v, path):
    res = False
    res = ([u, v] in path)
    if (not res):
        res = ([v, u] in path)
    return res

def randomlyChangeOneEdge(g):
    u = randint(0, len(g)-1)
    v = randint(0, len(g)-1)
    flip = False
    while (math.isinf(g[u][v])):
        if (not flip):
            v = randint(0, len(g)-1)
        elif (flip):
            u = randint(0, len(g)-1)
        flip = not flip
    newDist = randint(1, MAX_RANDOM_TIME)
    return [u, v, newDist]
    
if __name__ == "__main__":
    if (not USE_G):
        g = makeRandomGraph()
    
    print("n=" + str(len(g)))
    print("s=" + str(s))
    print("t=" + str(t))
    print()
    printGraph(g)
    print()

    edge_info = []
    for i in range(0, len(g)):
        edge_info.append([None, None])
    edge_info = dijkstra(g, edge_info, s)
    path = makePath(edge_info, s, t)
    totalDist = 0

    print("Shortest path from current position " + str(path[0][0]) + ":")
    printPath(path)
    dist = 0
    for edge in path:
        dist += g[edge[0]][edge[1]]
    print("Estimated time remaining: " + str(dist))
    travEdge = path.pop(0)
    totalDist += g[travEdge[0]][travEdge[1]]
    print("Traversed: " + str(travEdge))
    print("Time elapsed: " + str(totalDist))
    print()

    while (path):
        w = []
        while (True):
            w.append(randomlyChangeOneEdge(g))
            rand = uniform(0.0, 1.0)
            if (rand > MULTI_CHANGE_PROB):
                break
        
        #u, v, newDist = randomlyChangeOneEdge(g)
        for change in w:
            u = change[0]
            v = change[1]
            newDist = change[2]
            print("Traffic change: (" + str(u) + ", " + str(v) + ") = " + str(newDist))
        
        edge_info, path = dynamicShortestPath(g, edge_info, path, w)  
        print("Shortest path from current position " + str(path[0][0]) + ":")
        printPath(path)
        dist = 0
        for edge in path:
            dist += g[edge[0]][edge[1]]
        print("Estimated time remaining: " + str(dist))
        travEdge = path.pop(0)
        totalDist += g[travEdge[0]][travEdge[1]]
        print("Traversed: " + str(travEdge))
        print("Time elapsed: " + str(totalDist))
        print()
        
        #input()

    print("You have arrived at your destination.")
    print("Total time elapsed = " + str(totalDist))
