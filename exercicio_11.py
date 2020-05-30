'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Problema:
Dados n > 0 e uma sequência com n números reais, imprimí-los na ordem inversa a da leitura.
'''

n = int(input('Digite n: '))

lista = []
lista_reversa = []

# i = 0

# while i < n:
#   num = float(input('Digite o %dº. número: '%(i+1)))
#   lista.append(num)
#   i += 1

# i = len(lista) - 1
# while i >= 0:
#   lista_reversa = list(lista)
#   print(lista_reversa[i], end=' ')
#   i -= 1
# print()

# i = -1

# while i >= -n:
#   lista_reversa = list(lista)
#   print(lista_reversa[i], end=' ')
#   i -= 1
# print()

for i in range(n):
  num = float(input('Digite o %dº. número: '%(i+1)))
  lista = lista + [num]

# o fim vai até um número antes, ou seja, se você colocar -1, o programa para em 0
# for i in range(n-1, -1, -1):
#   lista_reversa = list(lista)
#   print(lista_reversa[i], end=' ')
# print()

for i in range(-1, -n-1, -1):
  lista_reversa = list(lista)
  print(lista_reversa[i], end=' ')
print()
