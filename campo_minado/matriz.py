"""
Funções para se trabalhar com matrizes.
"""

import random


def cria_matriz(m, n, valor):
    M = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(valor)
        M.append(linha)
    return M


def imprime_matriz(A):
    m = len(A)
    n = len(A[0])
    for i in range(m):
        for j in range(n):
            print("%7.2f" % (A[i][j]), end=" ")
        print()


def embaralha_matriz(matriz):
    m = len(matriz)
    n = len(matriz[0])

    for i in range(m):
        for j in range(n):
            x = random.randrange(0, n)
            y = random.randrange(0, m)
            tmp = matriz[i][j]
            matriz[i][j] = matriz[y][x]
            matriz[y][x] = tmp
