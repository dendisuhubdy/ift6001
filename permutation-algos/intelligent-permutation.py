def product(p, q):
    return tuple(q[p[i] - 1] for i in range(len(p)))

def inverse(p):
    q = [0] * (len(p)+1)
    for i in range(len(p)):
        q[p[i-1]] = i + 1
    return q

def sift(tableau, p):
    IDENTITY = tuple(range(1, len(p)+1))
    q=p
    while q is not IDENTITY:
        print(q)
        i = min(x for x in range(len(q)))
        j = q[i] - 1
        if tableau[i][j] == IDENTITY:
            tableau[i][j] = q
            return q
        else:
            #print("table")
            #print(tableau)
            q = product(q, inverse(tableau[i][j])) # inverse(tableau[i][j]))
            #print(len(q))
    return None

def appartenance_intelligent(permutations, r):
   IDENTITY = tuple(range(1, len(r)+1))
   tableau = [[IDENTITY] * len(r) for _ in range(len(r))]
   # Tamisage initial / Initial sift
   for p in permutations:
        sift(tableau, p)
   # Remplir tableau / Fill table
   to_sift = [(p, q) for p in permutations for q in permutations]
   while len(to_sift) > 0:
        p, q = to_sift.pop()
        q = sift(tableau, product(p, q))
        if q is not None:
         # q est une nouvelle permutation ajoutee au tableau
            to_sift.extend([(p, q) for p in permutations])
            to_sift.extend([(q, p) for p in permutations])
   # Genere r? / Generates r?
   return sift(tableau, r) is None

def main():
    # Exemple / Example
    a = tuple([2, 1, 3, 4, 5]) # (12)(3)(4)(5)
    b = tuple([2, 3, 4, 5, 1]) # (12345)
    r = tuple([2, 1, 4, 5, 3]) # (12)(345)
    print(appartenance_intelligent(set([a,b]), r))

if __name__=="__main__":
    main()
