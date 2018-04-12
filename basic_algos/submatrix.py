import math

def submatrix(A, i, j):
    return [[A[x][y] for y in range(len(A)) if y!= j] for x in range(len(A)) if x!=i]

def det(A):
    i = 0
    s = 0
    if len(A) == 1:
        return A[0][0]
    else:
        for j in range(len(A)):
            s += (-1)**(i+j) * A[i][j] * det(submatrix(A,i,j))
            return s

def main():
    A = [[1,2,3],[1,3,2],[6,5,2]]
    print(det(A))

if __name__=="__main__":
    main()
