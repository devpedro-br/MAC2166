'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Problema:
Sabe-se que cada número da forma n**3 é igual a soma de n ímpares consecutivos.

Exemplos:
1**3 = 1,
2**3 = 3 + 5,
3**3 = 7 + 9 + 11,
4**3 = 13 + 15 + 17 + 19.

Dado um número inteiro m, m > 0, determinar os ímpares consecutivos cuja soma é igual a n**3, para n assumindo valores de 1 a m.
'''

m = int(input('Digite m: '))

n = 1

while n <= m:
  soma = 0
  inicio = -1
  while soma != n**3:
    inicio += 2
    soma = ((inicio + inicio + (n - 1)*2)*(n))//2
      
  print('%d**3'%n, '=', inicio, end=' ')
  i = 2
  impar = inicio + 2

  while i <= n:
    print('+', impar, end=' ')
    impar += 2
    i += 1

  print()
  n += 1
