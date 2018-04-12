import math

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def ppcm(a, b):
    return a*b // pgcd(a, b)


def main():
    a = 10
    b = 100
    print(pgcd(a, b))
    print(ppcm(a,b))

if __name__=="__main__":
    main()

