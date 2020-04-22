# x = float(input('Digite x: '))
# y = float(input('Digite y: '))

# dentro = True

# abs_x = abs(x)












# # verificando se (x, y) está fora da face
# if y >= 8 or y <= 0 or x <= -5 or x >= 5:
#   dentro = False
# # verificando se (x, y) está na boca
# elif 1 <= y <= 2 and -3 <= x <= 3:
#   dentro = False
# # verificando se (x, y) está no olho direito
# elif 1 <= x <= 4 and 4 <= y <= 7:
#   dentro = False
#   # verificando se (x, y) está na iris direita
#   if 5 < y < 6 and 2 <x <3:
#     dentro = True
# # verificando se (x, y) está no olho esquerdo
# elif -4 <= x <= -1 and 4 <= y <= 7:
#   dentro = False
#   # verificando se (x, y) está na iris direita
#   if 5 < y < 6 and -3 < x < -2:
#     dentro = True


# if dentro:
#   print('Dentro')
# else:
#   print('Fora')
def testa_ponto(x, y):
  dentro = True

  abs_x = abs(x)
  # verificando se (x, y) está fora da face
  if y >= 8 or y <= 0 or abs_x >= 5:
    dentro = False
  # verificando se (x, y) está na boca
  elif 1 <= y <= 2 and abs_x <= 3:
    dentro = False
  # verificando se (x, y) está no olho direito
  elif 1 <= abs_x <= 4 and 4 <= y <= 7:
    dentro = False
    # verificando se (x, y) está na iris direita
    if 5 < y < 6 and 2 < abs_x <3:
      dentro = True

  return dentro

y = 8.0

while y >= 0.0:
  x = -5.0
  while x <= 5:
    if testa_ponto(x,y):
      print('π', end='')
    else:
      print('.', end='')
    x += 0.25
  print()
  y -= 0.25
