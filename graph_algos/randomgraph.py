import random

def random_graph(n):
    g = [[random.randint(0,1) for i in range(n)] for j in range(n)]
    for i in range(n):
        g[i][i] = 0
    for i in range(n):
        for j in range(n):
            g[j][i] = g[i][j]
    return g
