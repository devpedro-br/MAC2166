'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Problema:
Dado um número inteiro n (n > 1), imprimir sua decomposição em fatores primos, indicando também a multiplicidade de cada fator.

Por exemplo, para n = 600, a saída deverá ser:
fator 2 multiplicidade 3
fator 3 multiplicidade 1
fator 5 multiplicidade 2
'''

n = int(input('Digite n: '))

fator = 2

while n > 1:
  mult = 0

  while n % fator == 0:
    n = n // fator
    mult += 1

  if mult > 0:
    print('fator', fator, 'multiplicidade', mult)
    
  fator += 1
