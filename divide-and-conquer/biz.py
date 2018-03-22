import math
import sys

def biz(n):
    if (n < 2 and n>=0):
        return n
    else:
        print("double call to biz")
        return(biz(math.floor(n/2)) * biz(math.floor(n/4)))

if __name__=="__main__":
    s = biz(float(sys.argv[1]))
    print(s)
