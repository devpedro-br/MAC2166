'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Problema:
Nota: Questão 1 da Prova 1 de 2014.
Na figura, no plano cartesiano, a região sombreada não inclui as linhas de bordo. Note que o eixo y cai bem no meio da figura, e usamos o lado do quadrado para indicar as ordenadas correspondentes.

Escreva um programa que lê as coordenadas cartesianas (x, y) de um ponto, ambas do tipo float e imprime dentro se esse ponto está na região, e fora caso contrário.

Resultado esperado:
.........................................
.πππππππππππππππππππππππππππππππππππππππ.
.πππππππππππππππππππππππππππππππππππππππ.
.πππππππππππππππππππππππππππππππππππππππ.
.πππ.............πππππππ.............πππ.
.πππ.............πππππππ.............πππ.
.πππ.............πππππππ.............πππ.
.πππ.............πππππππ.............πππ.
.πππ.............πππππππ.............πππ.
.πππ.....πππ.....πππππππ.....πππ.....πππ.
.πππ.....πππ.....πππππππ.....πππ.....πππ.
.πππ.....πππ.....πππππππ.....πππ.....πππ.
.πππ.............πππππππ.............πππ.
.πππ.............πππππππ.............πππ.
.πππ.............πππππππ.............πππ.
.πππ.............πππππππ.............πππ.
.πππ.............πππππππ.............πππ.
.πππππππππππππππππππππππππππππππππππππππ.
.πππππππππππππππππππππππππππππππππππππππ.
.πππππππππππππππππππππππππππππππππππππππ.
.πππππππππππππππππππππππππππππππππππππππ.
.πππππππππππππππππππππππππππππππππππππππ.
.πππππππππππππππππππππππππππππππππππππππ.
.πππππππππππππππππππππππππππππππππππππππ.
.πππππππ.........................πππππππ.
.πππππππ.........................πππππππ.
.πππππππ.........................πππππππ.
.πππππππ.........................πππππππ.
.πππππππ.........................πππππππ.
.πππππππππππππππππππππππππππππππππππππππ.
.πππππππππππππππππππππππππππππππππππππππ.
.πππππππππππππππππππππππππππππππππππππππ.
.........................................
'''
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
