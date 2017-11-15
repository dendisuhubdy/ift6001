import numpy as np

def pdg(A):
        m = A.shape[0]
        p = [i for i in xrange(m)]
        while len(p)>1:
                i,j = p[0],p[1]
                if A[i,j] == 1:
                        p.remove(i)
                else:
                        p.remove(j)
        pdg = p[0]
        for i in xrange(m):
                if not i==pdg:
                        if A[i,pdg]==0 or A[pdg,i]==1:
                                print False
                                return False
        print True, pdg
        return True

def test():
    print 'testing with the random matrix'
    pdg(A)
    ### make an artificial PDG:
    print 'testing with a random artificially created PDG'
    newpdg = np.random.randint(A.shape[0])
    A[:,newpdg] = 1
    A[newpdg,:] = 0
    A[newpdg,newpdg] = 1
    pdg(A)
    print newpdg

def main():
    A = np.random.binomial(1,0.5,size=((10,10)))
    print A
    pdg(A)

if __name__=="__main__":
    main()
