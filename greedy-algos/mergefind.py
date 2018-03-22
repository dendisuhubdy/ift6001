def find(D, x):
    S, _ = D
    r = x
    while S[r] != r:
        r = S[r]
    return r

def merge(D, a, b):
    S, H = D
    if H[a] == H[b]:
        H[a] = H[a] + 1
        S[b] = a
    elif H[a] > H[b]:
        S[b] = a
    else:
        S[a] = b


