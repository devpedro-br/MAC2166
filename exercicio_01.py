'''
Autor: Pedro Lucas

Problema:
Dados um número inteiro n (n > 0) e um dígito d (0 <= d <= 9), determinar quantas vezes d ocorre em n.

Exemplos:
O dígito 3 ocorre 2 vezes em 63543
O dígito 0 ocorre 3 vezes em 10100
'''

n = int(input("Digite um número (n > 0): "))
num = n

d = int(input("Digite um dígito (0 <= d <= 9): "))

conta = 0

while n > 0:
  r = n % 10
  n = n // 10
  if r == d:
    conta += 1

print("\nO dígito", d, "ocorre", conta, "vezes em", num)
