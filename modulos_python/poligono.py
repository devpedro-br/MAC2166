'''
Módulo auxiliar do arquivo desenho.py
'''

import ponto
import turtle
import math
 
def perimetro(Pol):
    """Calcula o perímetro de um polígono Pol = [P1, P2, ..., Pn] composto por n pontos."""
    peri = 0.0 # perímetro
    Pant = Pol[-1] # ponto anterior
    for P in Pol:
        dist = ponto.distancia(Pant, P)
        peri += dist
        Pant = P
    
    return peri

def PorPontoMedio(Pol):
  PolPM = []
  Pant = Pol[-1] # ponto anterior
  for P in Pol:
    PM = ponto.pontomedio(Pant, P)
    PolPM.append(PM)
    Pant = P
  
  return PolPM

def desenha(Pol):
  Pant = Pol[-1] # ponto anterior
  turtle.penup()
  turtle.setpos(Pant)
  turtle.pendown()
  for P in Pol:
    dx = P[0] - Pant[0]
    dy = P[1] - Pant[1]
    angulo = math.atan2(dy, dx) * (180.0/math.pi)
    turtle.setheading(angulo)
    dist = ponto.distancia(Pant, P)
    turtle.forward(dist)
    Pant = P
