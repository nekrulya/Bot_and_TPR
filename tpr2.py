import numpy as np



def print_matrix(matrix, number_of_vert, inf):
    pass


def Floyd(matrica, number_of_vert, path):
    for k in range(0, number_of_vert):
        for i in range(0, number_of_vert):
            for j in range(0, number_of_vert):
                matrica[i][j] = min(matrica[i][j], matrica[i][k] + matrica[k][j])
                path[i][j] = k
    print(matrica)
    print(path)


def main():
    matrix = np.loadtxt('text.txt', dtype=int)
    number_of_vert = matrix.shape[0]
    path = np.full(matrix.shape, np.inf)
    print(path)
    print(matrix.shape[0])
    print(matrix.shape)
    print(matrix)
    Floyd(matrix, number_of_vert, path)



if __name__ == '__main__':
    main()