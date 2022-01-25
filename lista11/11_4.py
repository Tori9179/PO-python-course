def multiply_matrices(matrix1, matrix2): # liczba kolumn równa liczbie wierszy
    matrix3 = [[0 for i in range(len(matrix1[0]))] for j in range(len(matrix1))]
    matrix4 = [[], []]
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                for k in range(len(matrix2)):
                    matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
        return matrix3
    else:
        return matrix4


def print_matrix(matrix):
    if matrix != [[], []]:
        for row in matrix:
            for value in row:
                print(value, end="\t")
            print()
        print()
    else:
        print([[], []])
        print()


A = [[3, 7], [6, 2]]
B = [[4, 5], [1, 3]]
print_matrix(A)
print_matrix(B)
print_matrix(multiply_matrices(A, B))
