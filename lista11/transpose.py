import numpy as np


def matrix_transpose(n, m):
    A = np.random.randint(0, 10, (m, n))
    B = np.empty([n, m], dtype=int)
    print(A)
    for i in range(0, n):
        for j in range(0, m):
            B[i][j] = A[j][i]
    print(B)
    A = A.transpose()
    return A


matrix_transpose(5, 8)
