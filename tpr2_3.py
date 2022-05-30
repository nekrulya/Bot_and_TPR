import random
import math
import itertools

# исключение вершин в которые нельзя попасть из первой
# записать индексы -1 к которым нет дороги
arr = [1, 2, 3, 7, 8]


def gen_matrix(arr):
    matrix_D = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    matrix_S = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(0, 9):
        for j in range(i, 9):
            if (i == j):
                matrix_D[i][j] = 0
            elif (i == 0 and (j in arr)):
                matrix_D[i][j] = math.inf
                matrix_D[j][i] = math.inf
            else:
                matrix_D[i][j] = random.randint(3, 10)
                matrix_D[j][i] = matrix_D[i][j] #- random.randint(1, 2) #для асимметрии
    for i in range(0, 9):
        for j in range(0, 9):
            if i == j:
                matrix_S[i][j] = math.inf
            else:
                matrix_S[i][j] = j + 1
    return matrix_D, matrix_S


def get_path(output_matrix_D, output_matrix_S):
    v = {0, 1, 2, 3, 4, 5, 6, 7, 8}
    paths = itertools.combinations(v, 2)
    for comb in paths:
        u = comb[0]
        v = comb[1]
        path = [u + 1]
        while u != v:
            u = output_matrix_S[u][v] - 1
            path.append(u + 1)
        print("Путь из " + str(comb[0] + 1) + " в " + str(comb[1] + 1) + ": " + str(path) + " ---------- Длина пути: " + str(output_matrix_D[comb[0]][comb[1]]))


def floyd_algorithm(D0, S0):
    for k in range(0, len(D0)):
        for i in range(len(D0)):
            for j in range(len(D0)):
                if (i == j):
                    pass
                if D0[i][k] + D0[k][j] < D0[i][j]:
                    D0[i][j] = D0[i][k] + D0[k][j]
                    S0[i][j] = k + 1
    print("----------------D" + str(k + 1) + "----------------")
    for row in D0:
        print(row)
    print("----------------------------------\n")
    print("----------------S" + str(k + 1) + "----------------")
    for row in S0:
        print(row)
    print("----------------------------------\n")
    get_path(D0, S0)


def print_floyd(arr):
    new_matrix_D, new_matrix_S = gen_matrix(arr)
    print("----------------D0----------------")
    for row in new_matrix_D:
        print(row)
    print("----------------------------------\n")
    print("----------------S0----------------")
    for row in new_matrix_S:
        print(row)
    print("----------------------------------\n")
    floyd_algorithm(new_matrix_D, new_matrix_S)



def GenMatrix(arr):
    matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    #Заполнение не симметрично
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix)):
            if i == j:
                matrix[i][j] = 0
            elif i == 0 and (j in arr):
                matrix[i][j] = 0
                matrix[j][i] = 0
            else:
                matrix[i][j] = random.randint(3, 10)
                matrix[j][i] = matrix[i][j] #- random.randint(1, 2) #для асимметрии

    for i in matrix:
       print(i)
    print("-------------------------------")

    dict_ = dict()
    for i in range(0, len(matrix)):
        row_dict = dict()
        for j in range(0, len(matrix)):
            if matrix[i][j] != 0:
                row_dict[j] = matrix[i][j]
        dict_[i] = row_dict
        #print(str(i) + ": " + str(row_dict))

    return dict_


def find_min(Q, w):
    m = 0
    minimum = w[0]
    for i in range(len(w)):
        if w[i] < minimum:
            minimum = w[i]
            m = i
    return Q[m]


def dijkstra(G, s):
    Q = [s]
    p = {s:None}
    w = [0]
    d = {}
    for i in G:
        d[i] = float('inf')
        Q.append(i)
        w.append(d[i])
    d[s]=0
    while Q:
        u = find_min(Q, w)
        Q.remove(u)
        for v in G[u]:
            if d[v] >= d[u]+G[u][v]:
                d[v] = d[u]+G[u][v]
                p[v] = u
    return d, p

def dextr(arr):
    G = GenMatrix(arr)
    start = int(input('Начало: ')) - 1 #делай - 1, если из 5ки в 9ку, то старт равен 4
    d_p = dijkstra(G, start)
    #print("-------------------------------")

    for i in range(0, len(d_p[0])):
        if i == start:
            print(str(i + 1) + " вершина: (расстояние: " + str(d_p[0][0]) + "; предыдущий узел: " + str(d_p[1][0]) + ")")
        else:
            print(str(i + 1) + " вершина: (расстояние: " + str(d_p[0][i]) + "; предыдущий узел: " + str(d_p[1][i] + 1) + ")" )
    print("-------------------------------")

    stop = int(input('Конец: ')) - 1 #делай - 1, если из 5ки в 9ку, то стоп равен 8
    way = [stop]
    length = d_p[0][stop]

    flag = True
    while flag:
        if d_p[1][way[-1]] == start:
            way.append(start)
            flag = False
        else:
            way.append(d_p[1][way[-1]])

    way = way[::-1]
    res = ''

    for i in range(len(way) - 1):
        res += str(way[i] + 1) + " -> "
    res += str(way[-1] + 1)

    print("Кратчайший путь: " + str(res))
    print("-------------------------------")
    print("Кратчайшее расстояние: " + str(length))
    print("-------------------------------")

def main():

    print_floyd(arr)
    dextr(arr)


if __name__ == "__main__":
    main()
