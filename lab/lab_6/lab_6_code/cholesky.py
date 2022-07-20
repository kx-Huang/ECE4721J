import os
import numpy as np

path_data = "data/"
paths = [os.path.join(path_data, f) for f in os.listdir(path_data)]


def read_matrix_from_file(path):
    print("---------- {} ----------".format(path))
    matrix = np.loadtxt(open(path, "rb"), delimiter='\t', ndmin=2)
    print("Input matrix A:")
    print(matrix)
    return matrix


def cholesky_decomposition(a):
    # check input is a valid matrix
    if a.shape[0] != a.shape[1]:
        exit("[Error] input is not a N x N matrix.")

    # Cholesky Decomposition
    n = a.shape[0]
    c = np.empty([n, n])

    for i in range(n):
        for j in range(i+1, n):
            c[i][j] = 0

    for j in range(n):
        c[j][j] = np.sqrt(a[j][j])
        for i in range(j+1, n):
            c[i][j] = a[i][j] / c[j][j]
            for k in range(j, i+1):
                a[i][k] = a[i][k] - c[i][j] * c[k][j]

    return c


if __name__ == '__main__':
    for path in paths:
        # get input matrix A
        input = read_matrix_from_file(path)

        # get matrix C with numpy method as reference
        print("Reference matrix C:")
        print(np.linalg.cholesky(input))

        # get output matrix C
        output = cholesky_decomposition(input)
        print("Output matrix C:")
        print(output)
