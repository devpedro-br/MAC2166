'''
Resolução do professor: Paulo Andre Vechiatto de Miranda
'''

L = int(input('Digite L: '))
M = int(input('Digite M: '))
y = (L * M) - 1

while y >= 0:
  x = 0
  while x < (L * M):
    tx = x % L
    ty = y % L

    expressao = tx + L//2 >= ty and ty + L//2 >= tx

    if (x//L + y//L) % 2 == 1:
      expressao = not expressao
    if expressao:
      print('π', end='')
    else:
      print('.', end='')
    x += 1
  print()
  y-= 1
