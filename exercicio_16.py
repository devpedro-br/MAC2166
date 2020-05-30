'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Problema:
a) Escreva uma função que recebe um número inteiro e retorna uma lista contendo os seus dígitos. Os dígitos podem estar em ordem reversa.

b) Escreva uma função que recebe uma lista e retorna uma lista contendo os seus elementos em ordem reversa.

c) Escreva uma função que recebe 2 listas (l1 e l2) e devolve True caso:
      l1 e l2 tem o mesmo tamanho e os elementos de l1 e l2 são todos iguais e na mesma ordem.
   Caso contrário, a função deve devolver False.

d) Escreva um programa que leia um número inteiro n > 0 e determina se ele é ou não palíndromo usando as funções anteriores. Um número inteiro é palíndromo se ele possui a mesma sequência de dígitos quando lido tanto da direita para a esquerda como da esquerda para a direita.
'''

def listaDigitos(n):
  L = []
  while n > 0:
    r = n % 10
    L.append(r)
    n = n // 10
  return L

'''
def ordemReversa(L):
  R = []
  i = len(L) - 1

  for i in range(len(L)-1, -1, -1):
    R.append(L[i])

  return R
'''

'''
def ordemReversa(L):
  n = len(L)
  R = [0] * n

  for i in range(n):
    R[i] = L[(n-1)-i]

  return R
'''

def ordemReversa(L):
  R = L[:]
  R.reverse()
  
  return R

'''
def testaIguais(l1, l2):
  if len(l1) != len(l2):
    return False
  for i in range(len(l1)):
    if l1[i] != l2[i]:
      return False
  
  return True
'''

def testaIguais(l1, l2):
  return l1 == l2

def main():
  n = int(input('Digite n: '))
  
  L = listaDigitos(n)
  R = ordemReversa(L)
  if testaIguais(L, R):
    print('%d é palíndromo'%n)
  else:
    print('%d não é palíndromo'%n)

main()
