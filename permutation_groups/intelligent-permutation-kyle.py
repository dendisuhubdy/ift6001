# code for AGM testing (abelian group membership test)
# from IFT6001, Prof. McKenzie
# TA'd by Maelle Zimmerman - code from her demonstration
# License: BSD 3-Clause

import pprint
pp = pprint.PrettyPrinter(indent=4)

def prodp(p, q):
    return tuple(q[p[i] - 1] for i in range(len(p)))

def invp(p):
    q = [0] * len(p)
    for i in range(len(p)):
        q[p[i] - 1] = i + 1
    return q

def sift(table, p):
    ident = tuple(range(1, len(p) + 1))
    q = p

    while q != ident:
        i = min(x for x in range(len(q)) if q[x] != x + 1)
        j = q[i] - 1
        if table[i][j] == ident:
            table[i][j] = q
            return q
        else:
            q = prodp(q, invp(table[i][j]))
    return None

def membership_fast(permutations, r):
    ident = tuple(range(1, len(r) + 1))
    table = [[ident] * len(r) for _ in range(len(r))]

    # Initial sift
    for p in permutations:
        sift(table, p)

    # fill table
    to_sift = [(p, q) for p in permutations for q in permutations]

    while len(to_sift) > 0:
        p, q = to_sift.pop()
        q = sift(table, prodp(p, q))

        if q is not None:
            # q is a new permutation added to table
            to_sift.extend([(p, q) for p in permutations])
            to_sift.extend([(q, p) for p in permutations])
    # generates r
    pp.pprint(table)
    return sift(table, r) is None

# stacked representation - each tuple is the bottom part
# with reference/identity order on top
# e.g.
# (1 2 3 4 5)
# (2 1 3 4 5) -> (12)(3)(4)(5) -> (12)
# and
# (1 2 3 4 5)
# (2 1 4 5 3) -> (12)(345)
a = tuple([2, 1, 3, 4, 5]) # (12)(3)(4)(5)
b = tuple([2, 3, 4, 5, 1]) # (12345)
r = tuple([2, 1, 4, 5, 3]) # (12)(345)

print(membership_fast(set([a, b]), r))
