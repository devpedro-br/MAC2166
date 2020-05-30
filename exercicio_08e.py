'''
Resolução do professor: Paulo Andre Vechiatto de Miranda
'''

L = int(input('Digite L: '))

y = L-1

while y >= 0:
  x = 0
  while x < L:
    if x + L//2 >= y and y + L//2 >= x:
      print('π', end='')
    else:
      print('.', end='')
    x += 1
  print()
  y-= 1
