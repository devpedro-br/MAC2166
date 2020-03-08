'''
Autor: Pedro Lucas

Problema:
Dizemos que um número inteiro positivo é triangular se ele é o produto de três números inteiros consecutivos.

Por exemplo, 120 é triangular, pois 4*5*6 é igual a 120. Dado um número inteiro positivo n, verificar se n é triangular.
'''

n = int(input("Digite um número (n > 0): "))

resul = 0
i = 0

while resul < n:
  resul = (i)*(i + 1)*(i + 2)
  if resul == n:
    print(n, "é triangular, pois", i, "*", (i + 1), "*", (i + 2), "é igual a", n)
  i = i + 1
