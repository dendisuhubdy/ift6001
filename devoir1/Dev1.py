# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:57:42 2017

@author: alessandro
"""

def product(p, q):
    return tuple(q[p[i] - 1] for i in range(len(p)))

def inverse(p):
    q = [0] * len(p)
    for i in range(len(p)):
        q[p[i]-1] = i + 1
    return q

def composition(perm, r):
    IDENTITY = tuple(range(1, len(r)+1))
    toDo = [(p, q) for p in perm for q in perm]

    while len(toDo)>0:
        (p, q) = toDo.pop()
        z = product(p,q)
        print(p)
        print('o')
        print(q)
        if z in perm:
            print('already got')
        else:
             toDo.extend([(p, z) for p in perm])
             toDo.extend([(z, p) for p in perm])
             perm.add(z)
             print('=')
             print(z)
             print()
             if z==r:
                 return True

    return r in perm

f11 = tuple([3,1,3,4])
f12 = tuple([3,4,2,1])
f13 = tuple([2,1,3,4])
s1 = set([f11,f12])
f1 = tuple([1,1,1,2])

print(composition(s1,f1))
