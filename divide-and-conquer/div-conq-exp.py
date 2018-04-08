import math

def deux(a):
    n = len(a)
    p = 0
    i = 0
    k = 0
    while k<n:
        if (math.floor(a[k]/2) == a[k]/2):
            p = p + 1
        else:
            i = i + 1

        k = k + 1

    return (p, i)

if __name__=="__main__":
    print(deux([1, 2, 3, 4]))
