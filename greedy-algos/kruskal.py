from mergefind import merge, find

def kruskal(V, E):
    T=[]
    def init(k):
        return (range(k), [0] * k)
    D = init(len(V))
    def poids((u, v, c)):
        return c

    for (u, v, c) in sorted(E, key=poids):
        i = find(D, u)
        j = find(D, v)
        if i!= j:
            merge(D, i, j)
            T.append((u,v))
        return T
