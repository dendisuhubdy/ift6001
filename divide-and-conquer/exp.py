import math

def un(a, n):
    k = 0
    b = 1
    while (k < n):
        k = k + 1
        b = b * a
        print(k, b)
    return b

if __name__=="__main__":
    print(un(4, 5))
