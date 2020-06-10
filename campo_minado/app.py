import matriz as ma
import random

# Constantes
MINA = -1
LIVRE = 0

NAO_ACESSADA = 0
ACESSADA = 1
BANDEIRA = 2

"""
def cria_campo_minado(m, n, nminas):
    Campo = ma.cria_matriz(m, n, LIVRE)
    i, j = 0, 0
    for k in range(nminas):
        Campo[i][j] = MINA
        j += 1
        if j == n:
            i += 1
            j = 0
    ma.embaralha_matriz(Campo)
    return Campo
"""


def cria_campo_minado(m, n, nminas):
    # Representação linearizada da matriz
    C = [MINA] * nminas + [LIVRE] * (m * n - nminas)
    random.shuffle(C)

    Campo = []
    for i in range(m):
        Campo.append(C[i * n : (i + 1) * n])
    return Campo


"""
def conta_minas(Campo, lin, col):
    conta = 0
    m = len(Campo)
    n = len(Campo[0])

    # (lin, col - 1)
    if conta - 1 >= 0:
        if Campo[lin][col - 1] == MINA:
            conta += 1
    
    # (lin + 1, col)
    if lin + 1 < m:
        if Campo[lin + 1][col] == MINA:
            conta += 1

    # (lin + 1, col - 1)
    if lin + 1 < m and col - 1 >= 0:
        if Campo[lin + 1][col - 1] == MINA:
            conta += 1
    return conta
"""

"""
# Feito especificamente para 8 vizinhos
def conta_minas(Campo, lin, col):
    conta = 0
    m = len(Campo)
    n = len(Campo[0])
    for i in range(lin - 1, lin + 2):
        for j in range(col - 1, col + 2):
            if i >= 0 and i < m and j >= 0 and j < n:
                if Campo[i][j] == MINA:
                    conta += 1
    return conta
"""

# Mais genérico
def conta_minas(Campo, lin, col):
    # Vetores para fazer o deslocamento
    Li = [0, 0, -1, 1, 1, -1, -1, 1]
    Lj = [1, -1, 0, 0, 1, -1, 1, -1]

    conta = 0
    m = len(Campo)
    n = len(Campo[0])

    for k in range(len(Li)):
        # (i, j) = (lin, col) + (di, dj)
        i = lin + Li[k]
        j = col + Lj[k]
        if i >= 0 and i < m and j >= 0 and j < n:
            if Campo[i][j] == MINA:
                conta += 1
    return conta


def conta_minas_campo(Campo):
    m = len(Campo)
    n = len(Campo[0])

    for i in range(m):
        for j in range(n):
            if Campo[i][j] == LIVRE:
                Campo[i][j] = conta_minas(Campo, i, j)


def testa_boom(Campo, Acesso):
    boom = False
    m = len(Campo)  # linhas
    n = len(Campo[0])  # colunas

    for i in range(m):
        for j in range(n):
            if Campo[i][j] == MINA and Acesso[i][j] == ACESSADA:
                boom = True
    return boom


def testa_vitoria(Campo, Acesso):
    vitoria = True
    m = len(Campo)  # linhas
    n = len(Campo[0])  # colunas

    for i in range(m):
        for j in range(n):
            if Campo[i][j] != MINA and Acesso[i][j] != ACESSADA:
                vitoria = False

    return vitoria


def imprime_tabuleiro(Campo, Acesso):
    m = len(Campo)  # linhas
    n = len(Campo[0])  # colunas

    boom = testa_boom(Campo, Acesso)

    for i in range(m):
        for j in range(n):
            if boom and Campo[i][j] == MINA:
                print("* ", end="")
            elif Acesso[i][j] == BANDEIRA:
                print("P ", end="")
            elif Acesso[i][j] == NAO_ACESSADA:
                print("? ", end="")
            else:  # Acesso[i][j] == ACESSADA
                print("%d " % (Campo[i][j]), end="")
        print()


def main():
    m = int(input("Digite m: "))
    n = int(input("Digite n: "))
    nminas = int(input("Digite o número de minas: "))

    Campo = cria_campo_minado(m, n, nminas)
    conta_minas_campo(Campo)
    Acesso = ma.cria_matriz(m, n, NAO_ACESSADA)

    imprime_tabuleiro(Campo, Acesso)

    continuar = True
    while continuar:
        lin = int(input("Digite lin: "))
        col = int(input("Digite col: "))
        band = input("Bandeira? (s/n) ")

        if band == "s":
            if Acesso[lin][col] == BANDEIRA:
                Acesso[lin][col] = NAO_ACESSADA

            elif Acesso[lin][col] == NAO_ACESSADA:
                Acesso[lin][col] = BANDEIRA
        else:
            if Acesso[lin][col] != BANDEIRA:
                Acesso[lin][col] = ACESSADA

        imprime_tabuleiro(Campo, Acesso)
        vitoria = testa_vitoria(Campo, Acesso)
        boom = testa_boom(Campo, Acesso)
        if vitoria or boom:
            continuar = False

    if vitoria:
        print("Parabéns!")
    else:
        print("BOOOOOOOOOOM!")


main()
