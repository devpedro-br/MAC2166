'''
Utilizando módulos criados pelo programador em python.
'''

# modulo.__name__ # retorna o nome do módulo
import poligono
import turtle

def desenhar(Pol, Ninter):
  '''
  Ninter = número de interações
  '''
  poligono.desenha(Pol)

  while Ninter > 0:
    PolPm = poligono.PorPontoMedio(Pol)
    poligono.desenha(PolPm)
    Pol = PolPm
    Ninter -= 1

def main():
  screen = turtle.Screen()
  screen.setup(width = 1.0, height = 1.0)
  turtle.pensize(3)
  turtle.speed(3)
  turtle.hideturtle()
  turtle.pencolor('black')

  ajustar_x = -250
  ajustar_y = -50

  n = 0

  Pol_V = [
          [0 + ajustar_x, 400 + ajustar_y],
          [40 + ajustar_x, 250 + ajustar_y],
          [60 + ajustar_x, 250 + ajustar_y],
          [100 + ajustar_x, 400 + ajustar_y],
          [75 + ajustar_x, 400 + ajustar_y],
          [50 + ajustar_x, 300 + ajustar_y],
          [25 + ajustar_x, 400 + ajustar_y]]
  desenhar(Pol_V, n)

  Pol_A_externo = [
          [140 + ajustar_x, 400 + ajustar_y],
          [140 + ajustar_x, 250 + ajustar_y],
          [165 + ajustar_x, 250 + ajustar_y],
          [165 + ajustar_x, 325 + ajustar_y],
          [215 + ajustar_x, 325 + ajustar_y],
          [215 + ajustar_x, 250 + ajustar_y],
          [240 + ajustar_x, 250 + ajustar_y],
          [240 + ajustar_x, 400 + ajustar_y]]
  desenhar(Pol_A_externo, n)

  Pol_A_interno = [
          [165 + ajustar_x, 380 + ajustar_y],
          [165 + ajustar_x, 345 + ajustar_y],
          [215 + ajustar_x, 345 + ajustar_y],
          [215 + ajustar_x, 380 + ajustar_y]]
  desenhar(Pol_A_interno, n)

  Pol_M = [
          [280 + ajustar_x, 400 + ajustar_y],
          [280 + ajustar_x, 250 + ajustar_y],
          [305 + ajustar_x, 250 + ajustar_y],
          [305 + ajustar_x, 355 + ajustar_y],
          [320 + ajustar_x, 320 + ajustar_y],
          [340 + ajustar_x, 320 + ajustar_y],
          [355 + ajustar_x, 355 + ajustar_y],
          [355 + ajustar_x, 250 + ajustar_y],
          [380 + ajustar_x, 250 + ajustar_y],
          [380 + ajustar_x, 400 + ajustar_y],
          [355 + ajustar_x, 400 + ajustar_y],
          [330 + ajustar_x, 345 + ajustar_y],
          [305 + ajustar_x, 400 + ajustar_y]]
  desenhar(Pol_M, n)
  
  Pol_O_externo = [
          [420 + ajustar_x, 400 + ajustar_y],
          [420 + ajustar_x, 250 + ajustar_y],
          [520 + ajustar_x, 250 + ajustar_y],
          [520 + ajustar_x, 400 + ajustar_y]]
  desenhar(Pol_O_externo, n)

  Pol_O_interno = [
          [445 + ajustar_x, 375 + ajustar_y],
          [445 + ajustar_x, 275 + ajustar_y],
          [495 + ajustar_x, 275 + ajustar_y],
          [495 + ajustar_x, 375 + ajustar_y]]
  desenhar(Pol_O_interno, n)

  turtle.pencolor('red')
  turtle.speed(4)
  ajustar_x = -100
  ajustar_y = -50

  Pol_C = [
          [-300 + ajustar_x, -200 + ajustar_y],
          [-100 + ajustar_x, -200 + ajustar_y],
          [-100 + ajustar_x, -150 + ajustar_y],
          [-250 + ajustar_x, -150 + ajustar_y],
          [-250 + ajustar_x, 150 + ajustar_y],
          [-100 + ajustar_x, 150 + ajustar_y],
          [-100 + ajustar_x, 200 + ajustar_y],
          [-300 + ajustar_x, 200 + ajustar_y]]
  desenhar(Pol_C, n)

  Pol_A_externo = [
          [0 + ajustar_x, -200 + ajustar_y],
          [50 + ajustar_x, -200 + ajustar_y],
          [50 + ajustar_x, -50 + ajustar_y],
          [150 + ajustar_x, -50 + ajustar_y],
          [150 + ajustar_x, -200 + ajustar_y],
          [200 + ajustar_x, -200 + ajustar_y],
          [200 + ajustar_x, 200 + ajustar_y],
          [0 + ajustar_x, 200 + ajustar_y]]
  desenhar(Pol_A_externo, n)

  Pol_A_interno = [
          [50 + ajustar_x, 0 + ajustar_y],
          [150 + ajustar_x, 0 + ajustar_y],
          [150 + ajustar_x, 150 + ajustar_y],
          [50 + ajustar_x, 150 + ajustar_y]]
  desenhar(Pol_A_interno, n)

  Pol_M = [
          [300 + ajustar_x, -200 + ajustar_y],
          [350 + ajustar_x, -200 + ajustar_y],
          [350 + ajustar_x, 100 + ajustar_y],
          [400 + ajustar_x, 0 + ajustar_y],
          [500 + ajustar_x, 0 + ajustar_y],
          [550 + ajustar_x, 100 + ajustar_y],
          [550 + ajustar_x, -200 + ajustar_y],
          [600 + ajustar_x, -200 + ajustar_y],
          [600 + ajustar_x, 200 + ajustar_y],
          [550 + ajustar_x, 200 + ajustar_y],
          [450 + ajustar_x, 50 + ajustar_y],
          [350 + ajustar_x, 200 + ajustar_y],
          [300 + ajustar_x, 200 + ajustar_y]]
  desenhar(Pol_M, n)

  print()
main()
