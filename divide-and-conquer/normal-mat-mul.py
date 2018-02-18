"""
This is the normal matrix multiplication algorithm
that takes O(n^3) time complexity
"""

def matmul(A, B):
    n = len(A[0])
    print(n)
    C = [[],[]]
    for i in range(n):
        print(i)
        for j in range(n):
            print(j)
            C[i][j] = 0
            for k in range(n):
                print(k)
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C


def main():
    A = [[1,2],[3, 5]]
    B = [[3, 6],[8, 9]]

    C = matmul(A, B)
    print(C)


if __name__=="__main__":
    main()
