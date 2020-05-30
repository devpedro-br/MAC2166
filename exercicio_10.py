'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Problema:
Dados um número inteiro n>0 e uma sequência com n números inteiros maiores do que zero, determinar o máximo divisor comum entre eles. Por exemplo, para a entrada:
  3 42 30 105
o seu programa deve escrever o número 3.
'''

def mdc(a, b):
  if a < b:
    a,b = b,a
  while b > 0:
    r = a % b
    a = b
    b = r
  return a

def main():
  n = int(input('Digite n: '))
  i = 1
  mdc_parcial = int(input('Digite um número: '))
  while i < n:
    num = int(input('Digite um número: '))
    mdc_parcial = mdc(mdc_parcial, num)
    i += 1
  print(mdc_parcial)
main()
