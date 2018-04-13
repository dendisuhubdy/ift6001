import random
from itertools import starmap
from operator import mul
import numpy as np

def multiply(first, second):
    result = np.dot(first, second)
    result = np.array(result)
    return result

def subtract(first, second):
    result = np.subtract(first, second)
    result = np.array(result)
    return result

def frievalds(A, B, C):
    # generate a random 1xn matrix
    P = []
    choices = [0,1]
    for i in range(len(A)):
        P.append(random.choice(choices))

    dimA = len(A)

    BP = np.empty([dimA, dimA])
    BP = multiply(B, P)

    ABP = np.empty([dimA, dimA])
    ABP = multiply(A, BP)

    CP = np.empty([dimA, dimA])
    CP = multiply(C, P)

    result = np.empty([dimA, dimA])
    result = subtract(ABP, CP)

    decision = True
    for i in range(len(result)):
        print(result[i])
        if result[i] != 0:
            return False

    return decision

def repeatFrievalds(A, B, C, k):
    for i in range(k):
        decision = frievalds(A, B, C)
        if decision == False:
            return False
            # matrices AB and C are not equal

    return True


if __name__=="__main__":

    A = [[2, 3],[3, 4]]
    B = [[1, 0],[1, 2]]
    C = [[6, 5],[8, 7]]

    print(repeatFrievalds(A, B, C, 10))
