def matrices(D):
    m = len(D)-1
    T = [ [0]*m for i in range(m)] P = [[-1]*m for i in range(m)]
    for i in reversed(range(m)):
        for j in range(i+1, m):
            c, pos = float("inf"), -1

            for k in range(i, j):
                d = T[i][k] + T[k+1][j] + D[i]*D[k+1]*D[j+1]

                if (d < c):
                    c, pos = d, k
                T[i][j] = c
                P[i][j] = pos

    return P
