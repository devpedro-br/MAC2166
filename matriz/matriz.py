'''
Funções para se trabalhar com matrizes.
'''

def cria_matriz(m, n, valor):
  linha = [valor]*n
  matriz = []
  for i in range(m):
    matriz.append(linha[:])
  return matriz

def imprime_matriz(A):
  m = len(A)
  n = len(A[0])
  for i in range(m):
    for j in range(n):
      print("%7.2f"%(A[i][j]), end=' ')
    print()

def clonar_matriz(A)
  B = []
  for i in range(len(A)):
    B.append(A[i][:])
  return B

def leia_matriz():
  A = []
  m = int(input('Digite o número de linhas: '))
  n = int(input('Digite o número de colunas: '))
  for i in range(m):
    linha = []
    for j in range(n)
      num = float(input('Digite o elemento (%d, %d): '%(i, j)))
      linha.append(num)
    A.append(linha)
  return A

def transposta(A):
  T = cria_matriz(len(A[0]), len(A), 0)
  for i in range(len(T)):
    for j in range(len(T[0])):
      T[i][j] = A[j][i]
  return T

def igualdade(A, B):
  if len(A) != len(B) or len(A[0]) != len(B[0]):
    return False
  for i in range(len(A)):
    for j in range(len(A[0])):
      if A[i][j] != B[i][j]:
        return False
  return True

def simetrica(A):
  if len(A) != len(A[0]):
    return False
  for i in range(len(A)):
    for j in range(i):
      if A[i][j] != A[j][i]:
        return False
  return True
