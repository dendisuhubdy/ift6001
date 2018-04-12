from even import even_one

def expomod(a, n, z):
    """
    Fast modular exponentiation
    computes a^n mod z
    """

    i = n
    r = 1
    x = a % z

    while i > 0:
        if not even_one(i):
            r = (r*x) % z
            x = (r**2) % z
            i = i/2
            print(r)
    return r

if __name__=="__main__":
    print(expomod(2, 2, 3))
