def nb_pieces(c, s, k):
    T = [[float("inf")] * (k+1) for i in range(sum(s)+1)]
    P = [0] + [p for i in range(len(c)) for p in [c[i]] * s[i]]

    for i in range(len(T)):
        T[i][0] = 0

    for i in range(1, len(T)):
        for j in range(1, k+1):
            a = T[i-1][j] if i > 0 else float("inf")
            b = T[i-1][j-c[P[i]]] if j >= c[P[i]] else float("inf")
            print(i, j, c[P[i]])
            T[i][j] = min(a, b+1)

    return T

def money(c, s, k):
    T = nb_pieces(c, s, k)
    P = [None] + [x for i in range(len(c)) for x in [i] * s[i]]
    
    p = [0] * len(c)
    j = k

    for i in reversed(range(1, len(T))):
        a = T[i-1][j]
        b = T[i-1][j-c[P[i]]] if j >= c[P[i]] else float("inf")
        if T[i][j] != a:
            p[P[i]] += 1
            j -= c[P[i]]

    return p

if __name__=="__main__":
    c = [1, 5, 10, 100]
    s = [10, 10, 10, 10]

    M = 54

    result = money(c, s, M)

    print(c)
    print(s)
    print(result)
