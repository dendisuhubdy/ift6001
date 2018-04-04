def nb_pieces(c, M):
    T = [[0]*(M+1) for i in range(len(c))]

    for i in range(len(c)):
        for j in range(1, M+1):
            a = T[i-1][j] if i > 0 else float("inf")
            b = T[i][j-c[i]] if j >= c[i] else float("inf")
            T[i][j] = min(a, b+1)

    return T

def money(c, M):
    p = [0] * len(c)
    T = nb_pieces(c, M)

    i,j = len(c)-1, M
    while (i, j) != (0, 0):
        a = T[i-1][j] if i>0 else float("inf")
        b = T[i][j-c[i]] if j>= c[i] else float("inf")
    
        print(T)

        if T[i][j] == a:
            i -= 1
        else:
            j -= c[i]
            p[i] += 1

    return p

if __name__=="__main__":
    c = [1, 5, 10, 100]
    M = 525

    print(c)
    result = money(c, M)

    print(result)
