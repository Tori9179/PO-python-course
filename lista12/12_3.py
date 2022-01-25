def gauss_method2(matrix):
    for j in range(min(len(matrix), len(matrix[0]))):
        for i in range(j, len(matrix)):
            if matrix[i][j] != 0:
                matrix[j], matrix[i] = matrix[i], matrix[j]
                break
        else:
            continue
        for value in range(j, len(matrix[j]))[::-1]:
            matrix[j][value] /= matrix[j][j]
        for i in set(range(len(matrix))).difference({j}):
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


A = [[3.0, 6.0, 1.0, 3.0], [3.0, 1.0, 2.0, 4.0], [1.0, 4.0, 1.0, 6.0], [4.0, 2.0, 1.0, 3.0]]
print_matrix(A)
print_matrix(gauss_method2(A))
