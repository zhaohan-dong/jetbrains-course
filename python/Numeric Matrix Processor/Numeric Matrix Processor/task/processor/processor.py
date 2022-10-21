#!/usr/bin/python3


def matrix_addition():
    a = []
    b = []
    dimensionA = [int(elem) for elem in input('Enter size of first matrix: ').split(" ")]
    # build matrix A
    print('Enter first matrix:')
    for i in range(dimensionA[0]):
        a.append([float(elem) for elem in input().split(" ")])
    dimensionB = [int(elem) for elem in input('Enter size of second matrix: ').split(" ")]
    # build matrix B
    print('Enter second matrix:')
    for i in range(dimensionB[0]):
        b.append([float(elem) for elem in input().split(" ")])
    if dimensionA != dimensionB:
        print('The operation cannot be performed.')
    else:
        for i in range(dimensionA[0]):
            for j in range(dimensionA[1]):
                a[i][j] = str(a[i][j] + b[i][j])
        for i in range(dimensionA[0]):
            print(' '.join(a[i]))


def multiply_number():
    a = []
    dimensionA = [int(elem) for elem in input('Enter size of matrix: ').split(' ')]

    # build matrix A
    print('Enter matrix:')
    for i in range(dimensionA[0]):
        a.append([float(elem) for elem in input().split(' ')])
    multiplier = float(input('Enter constant: '))
    for i in range(dimensionA[0]):
        for j in range(dimensionA[1]):
            a[i][j] = str(a[i][j] * multiplier)
    print('The result is:')
    for i in range(dimensionA[0]):
        print(' '.join(a[i]))


def matrix_dot_product():
    a = []
    b = []
    result = []
    dimensionA = [int(elem) for elem in input('Enter size of first matrix: ').split(' ')]
    print('Enter first matrix:')
    for i in range(dimensionA[0]):
        a.append([float(elem) for elem in input().split(' ')])
    dimensionB = [int(elem) for elem in input('Enter size of second matrix: ').split(' ')]
    print('Enter second matrix:')
    for i in range(dimensionB[0]):
        b.append([float(elem) for elem in input().split(' ')])

    # dot product
    if dimensionA[1] == dimensionB[0]:
        for i in range(dimensionA[0]):
            row = []
            for k in range(dimensionB[1]):
                elem = 0
                for j in range(dimensionA[1]):
                    elem += a[i][j] * b[j][k]
                row.append(str(elem))
            result.append(row)
        print('The result is:')
        for i in range(len(result)):
            print(' '.join(result[i]))
    else:
        print('The operation cannot be performed.')


def transpose_matrix():
    a = []
    result = []
    print('1. Main diagonal\n'
          '2. Side diagonal\n'
          '3. Vertical line\n'
          '4. Horizontal line')
    choice = input('Your choice: ')
    dimensionA = [int(elem) for elem in input('Enter matrix size: ').split(' ')]
    print('Enter matrix:')
    for i in range(dimensionA[0]):
        a.append([float(elem) for elem in input().split(' ')])

    # transposing
    if choice == '1':
        for j in range(dimensionA[1]):
            row = []
            for i in range(dimensionA[0]):
                elem = str(a[i][j])
                row.append(elem)
            result.append(row)
    if choice == '2':
        for i in range(dimensionA[0] - 1, -1, -1):
            row = []
            for j in range(dimensionA[1] - 1, -1, -1):
                elem = str(a[j][i])
                row.append(elem)
            result.append(row)
    if choice == '3':
        for i in range(dimensionA[0]):
            row = []
            for j in range(dimensionA[1] - 1, -1, -1):
                elem = str(a[i][j])
                row.append(elem)
            result.append(row)
    if choice == '4':
        result = []
        for i in range(dimensionA[0] - 1, -1, -1):
            for j in range(dimensionA[1]):
                a[i][j] = str(a[i][j])
            result.append(a[i])
    print('The result is:')
    for i in range(len(result)):
        print(' '.join(result[i]))


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        result = 0
        for j in range(len(matrix)):
            minor = [matrix[k][:j] + matrix[k][j + 1:] for k in range(1, len(matrix))]
            result += matrix[0][j] * pow(-1, j) * determinant(minor)
        return result


def determinant_input():
    a = []
    dimensionA = [int(elem) for elem in input('Enter matrix size: ').split(' ')]

    # build matrix A
    print('Enter matrix:')
    for i in range(dimensionA[0]):
        a.append([float(elem) for elem in input().split(' ')])
    print('The result is:')
    print(determinant(a))


def main():
    while True:
        print('1. Add matrices\n'
              '2. Multiply matrix by a constant\n'
              '3. Multiply matrices\n'
              '4. Transpose matrix\n'
              '5. Calculate a determinant\n'
              '0. Exit')
        choice = input('Your choice')
        if choice == '1':
            matrix_addition()
        elif choice == '2':
            multiply_number()
        elif choice == '3':
            matrix_dot_product()
        elif choice == '4':
            transpose_matrix()
        elif choice == '5':
            determinant_input()
        elif choice == '0':
            break
    return 0


if __name__ == '__main__':
    main()
