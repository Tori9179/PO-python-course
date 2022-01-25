from random import randint


def random_matrix(rows, columns, item_range):
    matrix = [[randint(1, item_range) for _ in range(columns)] for _ in range(rows)]
    return matrix


def add_matrices(matrix1, matrix2):
    matrix3 = matrix1.copy()
    matrix4 = [[], []]
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        for i in range(len(matrix2)):
            for j in range(len(matrix2[0])):
                matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
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


print_matrix(random_matrix(5, 6, 99))
A = random_matrix(2, 7, 99)
B = random_matrix(2, 3, 99)
print_matrix(A)
print_matrix(B)
print_matrix(add_matrices(A, B))
