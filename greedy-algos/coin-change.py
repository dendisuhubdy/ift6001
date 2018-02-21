import sys

def makechange(n, C):
    # C is the denomination of coins available
    # n is the number that we need change from
    S = []
    s = 0 # sum of the coin numbers
    C = sorted(C, reverse=True)
    i = 0
    while s!=n:
        x = C[i]
        if s + x <= n:
            S.append(x)
            s = s + x
        else:
            i+=1
    return S


if __name__=="__main__":
    C = [100, 25, 10, 5, 1]
    n = int(sys.argv[1])
    S = makechange(n, C)

    print(S)


