import math

def insertionsort(alist):
    for i in range(1, len(alist)):
        x = alist[i]
        j = i - 1
        while j>=0 and x< alist[j]:
            alist[j+1] = alist[j]
            j = j-1
        alist[j+1] = x
    return alist

def main():
    list1 = [4,2,3,1]
    tup1 = (1,2,3,4)
    set1 = {1,2,3,4}

    tup2 = tuple([1,2,3,4])
    set1 = set([1,2,3,4])

    print(list1)
    print(insertionsort(list1))

if __name__=="__main__":
    main()
