def pgcd(a, b):
    while b:
        a, b = b, a%b
    return a

def ppcm(a, b):
    return a,b // pgcd(a, b)

def main():
    a = 213123
    b = 10210
    pgcd1 = pgcd(a,b)
    ppcm1 = ppcm(a,b)
    print(pgcd1)
    print(ppcm1)

if __name__=="__main__":
    main()
