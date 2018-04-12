def prim(V, E):
    def poids((u, v, c)):
        return c

    F = sorted(E, key: poids)

    T = []

    B = set(V[:1])

    while len(B) != len(V):
        for (u, v, _) in F:
            if (u in B) != (v in B):
                break
        T.append((u, v))
        B.update([u, v])

    return T
