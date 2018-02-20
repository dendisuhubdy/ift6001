"""__author__ = DENDI SUHUBDY"""


def product(tuple1, tuple2):
    result = tuple(tuple2[tuple1[i] - 1] for i in range(len(tuple1)))
    return result

def inverse(tuple_to_inverse):
    inverse_result = [0] * len(tuple_to_inverse)
    for i in xrange(tuple_to_inverse):
        inverse_result[tuple_to_inverse[i]-1] = i + 1
    return inverse_result

def composition(permutation, r, k):
    ID = tuple(range(1, len(r)+1))
    stopping_condition = [(p, q) for p in permutation for q in permutation]

    while len(stopping_condition)>k:
        (p, q) = stopping_condition.pop()
        z = product(p,q)
        #print(str(p) + ' o ' + str(q))
        if not(z in permutation):
             stopping_condition.extend([(p, z) for p in permutation])
             stopping_condition.extend([(z, p) for p in permutation])
             permutation.add(z)
             if z==r:
                 return True
    return r in permutation

def perm2(k, p, p1, p2):
    s1 = set([p1, p2])
    result = composition(s1, f1, k)
    return result

def main():
    k1 = 5
    p1 = (3,1,2,5,6,4)
    p11 = (2,3,4,5,6,1)
    p21 = (2,1,3,4,5,6)

    print("result of perm2(k1, p1, p11, p21) is ")
    result1 = perm2(k1, p1, p11, p21)
    print(result1)

    k2 = 15
    p2 = (3,1,2,5,6,4)
    p12 = (2,3,4,5,6,1)
    p22 = (2,1,3,4,5,6)

    print("result of perm2(k2, p2, p12, p22) is ")
    result2 = perm2(k2, p2, p12, p22)
    print(result2)

    k3 = 15
    p3 = (3,1,2,4,6,4)
    p13 = (2,3,4,5,6,1)
    p23 = (2,1,3,4,5,6)

    print("result of perm2(k3, p3, p13, p23) is ")
    result3 = perm2(k3, p3, p13, p23)
    print(result3)

    k4 = 35
    p4 = (5,3,9,6,7,2,1,8,4)
    p14 = (5,9,7,1,6,3,4,2,8)
    p24 = (8,1,2,9,5,4,3,7,6)

    print("result of perm2(k4, p4, p14, p24) is ")
    result4 = perm2(k4, p4, p14, p24)
    print(result4)

    k5 = 35
    p5 = (11,13,15,8,1,12,2,5,9,6,4,7,10,3,14)
    p15 = (2,15,4,5,3,11,9,6,7,13,1,14,10,8,12)
    p25 = (10,15,7,1,6,8,5,12,13,14,9,2,11,3,4)

    print("result of perm2(k5, p5, p15, p25) is ")
    result5 = perm2(k5, p5, p15, p25)
    print(result5)

    k6 = 35
    p6 = (9,15,11,8,13,10,1,12,3,4,5,6,7,2,14)
    p16 = (3,14,5,6,7,8,9,10,11,12,13,4,1,15,2)
    p26 = (15,9,13,8,12,7,6,2,10,3,14,1,11,4,5)

    print("result of perm2(k6, p6, p16, p26) is ")
    result6 = perm2(k6, p6, p16, p26)
    print(result6)

    k7 = 35
    p7 = (2,1,6,12,14,3,10,8,9,15,13,5,7,4,11)
    p17 = (15,9,13,8,12,7,6,2,10,3,14,1,11,4,5)
    p27 = (9,6,2,15,10,7,8,3,4,12,1,14,13,11,5)

    print("result of perm2(k7, p7, p17, p27) is ")
    result7 = perm2(k7, p7, p17, p27)
    print(result7)
