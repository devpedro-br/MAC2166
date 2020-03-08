'''
Autor: Pedro Lucas

Problema:
Qualquer número natural de quatro algarismos pode ser dividido em duas dezenas formadas pelos seus dois primeiros e dois últimos dígitos.

Exemplos:
1297: 12 e 97
5314: 53 e 14

Escreva um programa que imprime todos os milhares (4 algarismos) cuja raiz quadrada seja a soma das dezenas formadas pela divisão acima.

Exemplo:
raiz de 9801 = 99 = 98 + 01
'''

n = 1000
while n <= 9999:
  n_original = n
  r = n % 100
  j = n // 100
  soma = (r + j)
  resul = (soma)*(soma)
  if resul == n_original:
    print('Raiz de', n_original, "=", soma, "=", j, "+", r)
  n += 1
