def zero_matrix(rows, columns):
    matrix = [[0 for i in range(columns)] for j in range(rows)]
    return matrix


def identity_matrix(size):
    matrix = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                matrix[i][j] = 1
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end="\t")
        print()
    print()


print(zero_matrix(6, 5))
print(identity_matrix(5))
print_matrix(zero_matrix(6, 5))
print_matrix(identity_matrix(5))
