L = int(input('Digite L: '))

y = L-1

while y >= 0:
  x = 0
  while x < L:
    if x == y or (x + y) == (L-1): # or x == L//2 or y == L//2:
      print('π', end='')
    else:
      print('.', end='')
    x += 1
  print()
  y-= 1
