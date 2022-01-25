def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    total = 0
    for column, element in enumerate(matrix[0]):
        k = [x[:column] + x[column + 1:] for x in matrix[1:]]
        s = 1 if column % 2 == 0 else -1
        total += s * element * determinant(k)
    return total


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


A = [[1, 2, 3], [4, 5, 6], [7, 8, 12]]
print_matrix(A)
print(determinant(A))
