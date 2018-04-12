import random

def deterministic_distinct(L):
    L = sorted(L)
    for i in range(len(L)):
        if L[i] == L[i+1]:
            return False
    return True

def MC_distinct(L):
    for i in range(len(L)):
        i = random.randint(1, len(L)-1)
        j = random.randint(1, len(L)-1)

        if L[i] == L[j]:
            return False

    return True


if __name__=="__main__":
    A = [1, 2, 3, 1, 1, 4, 5]

    print(deterministic_distinct(A))

    print(MC_distinct(A))
