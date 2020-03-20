'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Problema:
Dado um número inteiro n (n > 0), verificar se este número contém dois dígitos adjacentes iguais.
'''

n = int(input('Digite n: '))

ant = n % 10

n = n // 10

adjiguais = False

while n > 0:
  r = n % 10

  if r == ant:
    adjiguais = True

  ant = r
  n = n // 10

if adjiguais:
  print('Possui adjacentes iguais')
else:
  print('Não possui adjacentes iguais')
