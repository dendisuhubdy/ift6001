from math import floor, log2

def myst(a, b):
    print("Function called")
    if (a < 4 and b<4):
        return (a + b)
    else:
        m       = int(floor(log2(max(a,b)))+1)
        shift   = m // 2
        r       = (2 ** shift)
        s, t    = a //r, a % r
        v, w    = b //r, b % r
        return (r * myst(s,v) + myst(t,w))


def main():
    a = 4
    b = 4

    result = myst(a, b)
    print(result)

    a = 16
    b = 8

    result = myst(a, b)
    print(result)

if __name__=="__main__":
    main()


