L = int(input('Digite L: '))
M = int(input('Digite M: '))
y = (L*M) - 1

while y >= 0:
  x = 0
  while x < (L * M):
    tx = x % L
    ty = y % L
    if tx == ty or (tx + ty) == (L-1):
      print('π', end='')
    else:
      print('.', end='')
    x += 1
  print()
  y-= 1
