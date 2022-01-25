def switch_rows(matrix, row1, row2):
    switched_matrix = matrix
    for i in range(len(switched_matrix)):
        for j in range(len(switched_matrix[0])):
            if i == row2:
                switched_matrix[row1], switched_matrix[row2] = switched_matrix[row2], switched_matrix[row1]
                break
    return switched_matrix


def multiply_row(matrix, row, value):
    new_matrix = matrix
    for i in range(0, len(new_matrix) + 1):
        if i == row:
            for j in range(len(new_matrix[0])):
                new_matrix[i][j] *= value
    return new_matrix


def add_row(matrix, row1, row2, amount):
    new_matrix = matrix
    for i in range(0, len(new_matrix) + 1):
        if i == row1:
            for j in range(len(new_matrix[0])):
                new_matrix[i][j] += new_matrix[row2][j] * amount
    return new_matrix


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


A = [[1, 2], [3, 4], [5, 6], [7, 8]]
print_matrix(A)
print_matrix(switch_rows(A, 0, 1))
print_matrix(multiply_row(A, 2, 3))
print_matrix(add_row(A, 3, 2, 4))
