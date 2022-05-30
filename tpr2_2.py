import math


V = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
     [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
     [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
     [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
     [10, math.inf, 3, 8, math.inf, math.inf, 1, 0]]


def print_matrix():
    for i in range(len(V)):
        print(V[i])


def get_path(P, v, u):
    path = [u]
    while u != v:
        u = P[u][v]
        path.append(u)

    return path


def Floyd():
    N = len(V)
    P = [[v for v in range(N)] for u in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                d = V[i][k] + V[k][j]
                if V[i][j] > d:
                    V[i][j] = d
                    P[i][j] = k

    start = int(input("Введите начальную вершину: "))
    end = int(input("Введите конечную вершину: "))
    for_print = get_path(P, start, end)
    for_print.reverse()
    print('Путь: ', for_print)


if __name__ == '__main__':
    print_matrix()
    Floyd()