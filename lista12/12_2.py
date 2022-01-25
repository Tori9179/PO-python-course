def rank_of_matrix(matrix):
    gauss_method(matrix)
    rank = 0
    for j in range(min(len(matrix), len(matrix[0]))):
        for i in range(j, len(matrix)):
            if matrix[i][j] != 0:
                rank += 1
                break
    return rank


def gauss_method(matrix):
    for j in range(min(len(matrix), len(matrix[0]))):
        for i in range(j, len(matrix)):
            if matrix[i][j] != 0:
                matrix[j], matrix[i] = matrix[i], matrix[j]
                break
        else:
            continue
        for value in range(j, len(matrix[j]))[::-1]:
            matrix[j][value] /= matrix[j][j]
        for i in range(j + 1, len(matrix)):
            for value in range(j, len(matrix[i]))[::-1]:
                matrix[i][value] -= matrix[j][value] * matrix[i][j]
    return matrix


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


A = [[1, 2, 3], [3, 4, 3], [5, 6, 5], [7, 8, 5]]
print_matrix(A)
print_matrix(gauss_method(A))
print(rank_of_matrix(A))
